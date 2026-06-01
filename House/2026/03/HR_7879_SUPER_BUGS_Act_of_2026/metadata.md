# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7879?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7879
- Title: SUPER BUGS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7879
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-01T08:08:14Z
- Update date including text: 2026-05-01T08:08:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7879",
    "number": "7879",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SUPER BUGS Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:14Z",
    "updateDateIncludingText": "2026-05-01T08:08:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7879ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7879\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Levin (for himself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State, in consultation with the Secretary of Health and Human Services and other relevant departments and agencies, as appropriate, to formulate a strategy for the Federal Government to secure support from foreign countries, multilateral organizations, and other appropriate entities to facilitate the development and commercialization of qualified pandemic or epidemic products, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Saving Us from Pandemic Era Resistance by Building a Unified Global Strategy Act of 2026 or the SUPER BUGS Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEmerging infectious diseases, including antimicrobial-resistant pathogens, pose a significant threat to United States national security by\u2014\n**(A)**\nincreasing the risk of outbreaks reaching the United States;\n**(B)**\ndisrupting critical infrastructure;\n**(C)**\nundermining economic stability and public health; and\n**(D)**\nundermining the readiness of the United States Armed Forces abroad.\n**(2)**\nStrengthening international collaboration to develop, commercialize, and deploy qualified pandemic and epidemic products is essential to preventing, detecting, and containing infectious disease threats before they reach the borders of the United States.\n**(3)**\nEnhancing partner countries\u2019 public health capabilities and pandemic and epidemic response mechanisms directly contributes to United States homeland security by reducing the likelihood of global outbreaks affecting the United States.\n**(4)**\nCoordinated strategies that leverage United States leadership, technology, and medical countermeasures, while ensuring equitable access for international partners, promote global resilience and reduce threats to United States citizens, infrastructure, and national interests.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(D)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Priority pathogens**\nThe term priority pathogens means pathogens identified in\u2014\n**(A)**\nthe latest Antibiotic Resistance Threats Report of the Centers for Disease Control and Prevention (or any successor report); or\n**(B)**\nthe current list of qualifying pathogens maintained by the Secretary of Health and Human Services under section 505E(f)(2) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355f(f)(2) ) (or any successor list).\n**(3) Qualified pandemic or epidemic product**\nThe term qualified pandemic or epidemic product has the meaning given such term in section 319F\u20133(i) of the Public Health Service Act (42 U.S.C. 247d\u20136d(i)).\n#### 4. International strategy for development of qualified pandemic or epidemic products\n##### (a) Strategy\n**(1) In general**\nNot later than 18 months after the date of the enactment of this Act, the Secretary of State, in consultation with the Secretary of Health and Human Services, and such other heads of departments and agencies as the Secretary of State considers appropriate, shall\u2014\n**(A)**\nformulate a strategy for the Federal Government to secure support from foreign countries, multilateral organizations, and other appropriate entities to facilitate the development and commercialization of qualified pandemic or epidemic products, including products to address antimicrobial resistant pathogens\u2014\n**(i)**\nwith pandemic potential; or\n**(ii)**\nthat are priority pathogens; and\n**(B)**\nsubmit such strategy to the appropriate committees of Congress.\n**(2) Contents**\nThe strategy required under paragraph (1) shall\u2014\n**(A)**\nprovide for processes the Federal Government is using and would use to enter into arrangements with foreign countries, multilateral organizations, and other appropriate entities in certain circumstances to implement the strategy;\n**(B)**\nstrive to ensure that the arrangements described in subparagraph (A) promote equitable contributions based on the budgets and technical expertise of participating countries, organizations, and other entities, as appropriate;\n**(C)**\nfocus the arrangements described in subparagraph (A) on global priorities, while enabling participating countries, organizations, and other entities to emphasize national or regional issues of importance;\n**(D)**\nsupport efforts to strengthen partner country public health capabilities by promoting sustainable improvements in their ability to prevent, detect, and contain infectious disease threats;\n**(E)**\nseek to ensure that new and existing arrangements described in subparagraph (A) are harmonized with each other and with other relevant existing or planned efforts to amplify impact, address gaps, prevent duplication of effort, and efficiently distribute funds;\n**(F)**\nprovide for collaboration to ensure the arrangements described in subparagraph (A) allocate joint or individual responsibility across participating countries, organizations, and other entities for the development and commercialization of particular qualified pandemic or epidemic products, where such collaboration is clearly described in such arrangement;\n**(G)**\nprovide for the stewardship of qualified pandemic or epidemic products developed pursuant to the strategy;\n**(H)**\nidentify priority actions in the arrangements described in subparagraph (A) so that scarce domestic and international funds are allocated to develop and commercialize qualified pandemic or epidemic products that can achieve the greatest positive impact on human health, including unprecedented approaches to preventing, treating, and diagnosing infectious diseases;\n**(I)**\nconsider securing contracts with United States companies and the broader private sector, entering into public-private partnerships, implementing alternative payment models, creating coverage and reimbursement pathways, and streamlining regulatory approval processes; and\n**(J)**\nbe synchronized with United States pandemic preparedness priorities, such as those articulated in\u2014\n**(i)**\nthe National Strategy for Combating Antibiotic-Resistant Bacteria (dated September 2014); and\n**(ii)**\nthe National Biodefense Strategy and Implementation Plan (dated October 2022) and the associated Action Plan (dated October 2022).\n##### (b) Arrangements with foreign countries and multilateral organizations\nThe Secretary of State, in consultation with the Secretary of Health and Human Services, and the heads of other relevant departments and agencies, as appropriate, shall seek to enter into arrangements with foreign countries, multilateral organizations, and other appropriate entities to implement the strategy required under subsection (a).",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-04-03T20:27:44Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7879ih.xml"
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
      "title": "SUPER BUGS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SUPER BUGS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Saving Us from Pandemic Era Resistance by Building a Unified Global Strategy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State, in consultation with the Secretary of Health and Human Services and other relevant departments and agencies, as appropriate, to formulate a strategy for the Federal Government to secure support from foreign countries, multilateral organizations, and other appropriate entities to facilitate the development and commercialization of qualified pandemic or epidemic products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:33Z"
    }
  ]
}
```
