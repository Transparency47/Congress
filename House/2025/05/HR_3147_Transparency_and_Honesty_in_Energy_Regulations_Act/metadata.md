# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3147?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3147
- Title: Transparency and Honesty in Energy Regulations Act
- Congress: 119
- Bill type: HR
- Bill number: 3147
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-09-09T08:05:58Z
- Update date including text: 2025-09-09T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-01 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3147",
    "number": "3147",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Transparency and Honesty in Energy Regulations Act",
    "type": "HR",
    "updateDate": "2025-09-09T08:05:58Z",
    "updateDateIncludingText": "2025-09-09T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-01T13:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "OH"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3147ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3147\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Hudson (for himself, Mr. Pfluger , and Mr. Balderson ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit Federal agencies from considering, in taking any action, the social cost of carbon, the social cost of methane, the social cost of nitrous oxide, or the social cost of any other greenhouse gas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transparency and Honesty in Energy Regulations Act .\n#### 2. Definitions\nIn this Act:\n**(1) Federal agency**\nThe term Federal agency means has the meaning given the term agency in section 551 of title 5, United States Code.\n**(2) Social cost of carbon**\nThe term social cost of carbon means\u2014\n**(A)**\nthe estimate of the social cost of carbon described in\u2014\n**(i)**\nthe document entitled Technical Support Document: Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866 , published by the Interagency Working Group on Social Cost of Carbon, United States Government, in February 2010;\n**(ii)**\nthe document entitled Technical Support Document: Social Cost of Carbon, Methane, and Nitrous Oxide Interim Estimates under Executive Order 13990 , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in February 2021;\n**(iii)**\nthe document entitled Technical Support Document: Technical Update of the Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866 , published by the Interagency Working Group on Social Cost of Carbon, United States Government, in May 2013 and revised in November 2013 and July 2015, and published and revised by the Interagency Working Group on the Social Cost of Greenhouse Gases, United States Government, in August 2016;\n**(iv)**\nthe document entitled Regulatory Impact Analysis for the New Source Performance Standards for Greenhouse Gas Emissions from New, Modified, and Reconstructed Fossil Fuel-Fired Electric Generating Units; Emission Guidelines for Greenhouse Gas Emissions from Existing Fossil Fuel-Fired Electric Generating Units; and Repeal of the Affordable Clean Energy Rule , published by the Administrator of the Environmental Protection Agency in April 2024;\n**(v)**\nthe document entitled Regulatory Impact Analysis for the Final Federal Good Neighbor Plan Addressing Regional Ozone Transport for the 2015 Ozone National Ambient Air Quality Standard , published by the Administrator of the Environmental Protection Agency in March 2023;\n**(vi)**\nthe document entitled Regulatory Impact Analysis for the Final National Emission Standards for Hazardous Air Pollutants: Coal- and Oil-Fired Electric Utility Steam Generating Units Review of the Residual Risk and Technology Review , published by the Administrator of the Environmental Protection Agency in April 2024;\n**(vii)**\nthe document entitled Benefit and Cost Analysis for Supplemental Effluent Limitations Guidelines and Standards for the Steam Electric Power Generating Point Source Category , published by the Administrator of the Environmental Protection Agency on April 18, 2024; or\n**(viii)**\nany successor or substantially related document; and\n**(B)**\nany other estimate of the monetized damages associated with an incremental increase in carbon dioxide emissions in a given year.\n**(3) Social cost of greenhouse gases**\nThe term social cost of greenhouse gases means\u2014\n**(A)**\nthe estimate of the social cost of any greenhouse gas that is described in\u2014\n**(i)**\nthe document entitled Technical Support Document: Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866 , published by the Interagency Working Group on Social Cost of Carbon, United States Government, in February 2010;\n**(ii)**\nthe document entitled Technical Support Document: Technical Update of the Social Cost of Carbon for Regulatory Impact Analysis Under Executive Order 12866 , published by the Interagency Working Group on Social Cost of Carbon, United States Government, in May 2013 and revised in November 2013 and July 2015, and published and revised by the Interagency Working Group on the Social Cost of Greenhouse Gases, United States Government, in August 2016;\n**(iii)**\nthe document entitled Addendum to Technical Support Document on Social Cost of Carbon for Regulatory Impact Analysis under Executive Order 12866: Application of the Methodology to Estimate the Social Cost of Methane and the Social Cost of Nitrous Oxide , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in August 2016;\n**(iv)**\nthe document entitled Technical Support Document: Social Cost of Carbon, Methane, and Nitrous Oxide Interim Estimates under Executive Order 13990 , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in February 2021; or\n**(v)**\nany successor or substantially related document; and\n**(B)**\nany other estimate of the monetized damages associated with an incremental increase in greenhouse gas emissions in a given year.\n**(4) Social cost of methane**\nThe term social cost of methane means\u2014\n**(A)**\nthe estimate of the social cost of methane described in\u2014\n**(i)**\nthe document entitled Addendum to Technical Support Document on Social Cost of Carbon for Regulatory Impact Analysis under Executive Order 12866: Application of the Methodology to Estimate the Social Cost of Methane and the Social Cost of Nitrous Oxide , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in August 2016;\n**(ii)**\nthe document entitled Technical Support Document: Social Cost of Carbon, Methane, and Nitrous Oxide Interim Estimates under Executive Order 13990 , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in February 2021;\n**(iii)**\nthe document entitled Benefit and Cost Analysis for Supplemental Effluent Limitations Guidelines and Standards for the Steam Electric Power Generating Point Source Category , published by the Administrator of the Environmental Protection Agency on April 18, 2024; or\n**(iv)**\nany successor or substantially related document; and\n**(B)**\nany other estimate of the monetized damages associated with an incremental increase in methane emissions in a given year.\n**(5) Social cost of nitrous oxide**\nThe term social cost of nitrous oxide means\u2014\n**(A)**\nthe estimate of the social cost of nitrous oxide described in\u2014\n**(i)**\nthe document entitled Addendum to Technical Support Document on Social Cost of Carbon for Regulatory Impact Analysis under Executive Order 12866: Application of the Methodology to Estimate the Social Cost of Methane and the Social Cost of Nitrous Oxide , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in August 2016;\n**(ii)**\nthe document entitled Technical Support Document: Social Cost of Carbon, Methane, and Nitrous Oxide Interim Estimates under Executive Order 13990 , published by the Interagency Working Group on Social Cost of Greenhouse Gases, United States Government, in February 2021; or\n**(iii)**\nany other successor or substantially related document; and\n**(B)**\nany other estimate of the monetized damages associated with an incremental increase in nitrous oxide emissions in a given year.\n#### 3. Prohibition on considering the social cost of greenhouse gases, including the social cost of carbon, the social cost of methane, and the social cost of nitrous oxide\nA Federal agency may not consider the social cost of carbon, social cost of methane, social cost of nitrous oxide, or social cost of greenhouse gases\u2014\n**(1)**\nas part of any cost-benefit or cost-effectiveness analysis required under\u2014\n**(A)**\nany law;\n**(B)**\nExecutive Order 12866 ( 5 U.S.C. 601 note; relating to regulatory planning and review); or\n**(C)**\nExecutive Order 13563 ( 5 U.S.C. 601 note; relating to improving regulation and regulatory review);\n**(2)**\nin any rulemaking;\n**(3)**\nin the issuance of any guidance;\n**(4)**\nin taking any other agency action; or\n**(5)**\nas a justification for any rulemaking, guidance document, or agency action.\n#### 4. Report to Congress\nNot later than 120 days after the date of the enactment of this Act, the head of each Federal agency shall submit to the Committees on Environment and Public Works and Energy and Natural Resources of the Senate and the Committees on Energy and Commerce and Natural Resources of the House of Representatives a report describing the number of proposed and final rulemakings, guidance documents, and agency actions that, since January 2009, have used the social cost of carbon, the social cost of greenhouse gases, the social cost of methane, or the social cost of nitrous oxide, including the use of the social cost of carbon, the social cost of greenhouse gases, the social cost of methane, or the social cost of nitrous oxide as part of any cost-benefit analysis required under Executive Order 12866 ( 5 U.S.C. 601 note; relating to regulatory planning and review) or other relevant authority.",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-06-23T16:59:01Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3147ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Transparency and Honesty in Energy Regulations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-13T09:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transparency and Honesty in Energy Regulations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal agencies from considering, in taking any action, the social cost of carbon, the social cost of methane, the social cost of nitrous oxide, or the social cost of any other greenhouse gas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T09:03:54Z"
    }
  ]
}
```
