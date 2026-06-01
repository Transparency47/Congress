# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6005
- Title: Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6005
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-22T08:07:37Z
- Update date including text: 2026-04-22T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-29 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6005",
    "number": "6005",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:37Z",
    "updateDateIncludingText": "2026-04-22T08:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-29T16:39:08Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6005ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6005\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mrs. Dingell introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the Sergeant First Class Heath Robinson Honoring our Promise to Address Comprehensive Toxics Act of 2022 to direct the Interagency Working Group on Toxic Exposure to conduct research on the diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving as members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025 .\n#### 2. Research on diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving in the Armed Forces\n##### (a) Interagency Working Group on Toxic Exposure Research\n**(1) Authority to establish interagency task forces**\nSubsection (b) of section 501 of the Sergeant First Class Heath Robinson Honoring our Promise to Address Comprehensive Toxics Act of 2022 ( Public Law 117\u2013168 ) is amended by adding at the end the following new paragraph:\n(3) Establish Federal interagency task forces to conduct collaborative research activities. .\n**(2) Reporting**\nSubsection (c) of such section is amended by striking paragraph (3) and inserting the following new paragraphs:\n(3) Not later than one year after the date of the enactment of the Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025 \u2014 (A) the findings of the members of the Working Group with respect to the collaborative research activities described in paragraph (2); (B) the strategic plan developed, by the Working Group under subsection (b); and (C) such recommendations as the Working Group may have for legislative or administrative action to improve collaborative research activities among the members of the Working Group. (4) Not less frequently than annually during the five-year period covered by the strategic plan developed under subsection (b)\u2014 (A) a summary of the collaborative research activities carried out by the members of the Working Group and the findings of the members with respect to such research activities; (B) a progress report on implementation of the strategic plan developed by the Working Group under subsection (b); and (C) such recommendations as the Working Group may have for legislative or administrative action to improve collaborative research activities among members of the Working Group. .\n**(3) Research requirements**\nSuch section is further amended\u2014\n**(A)**\nby redesignating subsections (c) through (e) as subsections (d) through (f), respectively;\n**(B)**\nin subsection (e), as redesignated by paragraph (1), by striking under subsection (c) and inserting under subsection (d) ; and\n**(C)**\nby inserting after subsection (b) the following new subsection (c):\n(c) Requirements relating to certain research on impacts to descendants The Working Group and the Agency for Toxic Substances and Disease Registry shall\u2014 (1) establish an interagency task force to conduct research on the diagnosis and treatment of health conditions of descendants of toxic-exposed veteran (as defined in section 101 of title 38, United States Code); (2) maintain a publicly available website with information on the activities and findings of the Agency under subparagraph (A), including a review of all relevant data to determine the strength of evidence for a positive association between a health condition researched and a toxic exposure risk activity (as defined in section 1710(e)(4) of title 38, United States Code) based on the categories set forth under section 1173(c)(2) of title 38, United States Code; and (3) perform other actions as directed by the Secretary. .\n##### (b) Study of descendants of veterans of Operation Ranch Hand\n**(1) Establishment**\nNot later than, the Secretary of Veterans Affairs shall conduct a study on the biological descendants of veterans who served in Operation Ranch Hand to\u2014\n**(A)**\nassess the rates of birth defects and developmental delays among such descendants; and\n**(B)**\nidentify\u2014\n**(i)**\ngenetic factors that prevented some of such descendants from developing such a birth defect or developmental delay;\n**(ii)**\ncauses of related health outcomes; and\n**(iii)**\npreventative measures to mitigate risks associated with toxic exposures.\n**(2) Participants**\nParticipation in the study shall be voluntary. To recruit participants, the Secretary shall contact such veterans and descendants.\n**(3) Data collection**\nTo carry out the study, the Secretary shall use\u2014\n**(A)**\nbiological samples from such veterans and descendants to which the Secretary has access;\n**(B)**\nhealth records of such veterans and descendants to which the Secretary has access; and\n**(C)**\nsurveys and questionnaires of such veterans and descendants, to identify relevant\u2014\n**(i)**\nenvironmental exposures;\n**(ii)**\nlifestyle factors; and\n**(iii)**\nhealth conditions.\n**(4) Data analysis**\nTo analyze data collected under subsection (c), the Secretary shall\u2014\n**(A)**\nuse statistical analysis (including regression models and comparative analyses) to determine correlations between toxic exposure and health outcomes; and\n**(B)**\nconduct genomic sequencing and analysis to identify genetic markers associated with health issues in such descendants.\n**(5) Report**\nNot later than, the Secretary shall publish the findings of the study.",
      "versionDate": "2025-11-10",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-23T15:04:39Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6005ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Sergeant First Class Heath Robinson Honoring our Promise to Address Comprehensive Toxics Act of 2022 to direct the Interagency Working Group on Toxic Exposure to conduct research on the diagnosis and treatment of health conditions of descendants of individuals exposed to toxic substances while serving as members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-23T07:54:14Z"
    },
    {
      "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-23T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Molly R. Loomis Research for Descendants of Toxic Exposed Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-23T04:38:19Z"
    }
  ]
}
```
