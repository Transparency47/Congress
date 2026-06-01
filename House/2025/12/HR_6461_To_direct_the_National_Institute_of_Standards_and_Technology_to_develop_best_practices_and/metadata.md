# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6461?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6461
- Title: READ AI Models Act
- Congress: 119
- Bill type: HR
- Bill number: 6461
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-08T08:06:29Z
- Update date including text: 2026-05-08T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6461",
    "number": "6461",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001238",
        "district": "",
        "firstName": "Sarah",
        "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
        "lastName": "McBride",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "READ AI Models Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:29Z",
    "updateDateIncludingText": "2026-05-08T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IN"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6461ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6461\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. McBride (for herself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the National Institute of Standards and Technology to develop best practices and technical guidance on artificial intelligence model documentation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Resources for Evaluating and Documenting AI Models or the READ AI Models Act .\n#### 2. Resources for artificial intelligence model documentation\n##### (a) Resources\n**(1) In general**\nSubject to the availability of appropriations, the Director of the National Institute of Standards and Technology, in consultation with the heads of other Federal agencies, as appropriate, shall initiate a pilot program to establish a structured template and associated technical guidelines for documentation to accompany artificial intelligence models and associated data developed and used by the public sector or private sector.\n**(2) Activities**\nSubject to the availability of appropriations, in carrying out paragraph (1), the Director shall carry out the following:\n**(A)**\nProduce a structured template designed to enable a user to document information about an artificial intelligence model and associated data, which may include the following information:\n**(i)**\nThe name of such model.\n**(ii)**\nThe identification of the developer of such model.\n**(iii)**\nThe identification of the location where such developer is incorporated.\n**(iv)**\nThe release date of such model.\n**(v)**\nThe knowledge cutoff date for such model\u2019s training data.\n**(vi)**\nLanguages supported by such model.\n**(vii)**\nTerms of service of such model.\n**(viii)**\nAny other information the Director determines appropriate.\n**(B)**\nEnsure such template is modular in nature, such that users can flexibly adopt and complete sections, categories, or other similar components of such template in accordance with a specific use case, including relating to sector-specific needs, intended audiences, and a set of desired characteristics.\n**(C)**\nProvide detailed technical guidelines accompanying such template that\u2014\n**(i)**\nmake available relevant metrics or benchmarks for each component of such template for a range of artificial intelligence model types, as applicable; and\n**(ii)**\nincorporate voluntary consensus-based technical standards and industry best practices, as appropriate.\n**(3) Stakeholder input**\nIn carrying out paragraph (2), the Director shall carry out the following:\n**(A)**\nCollaborate with private sector entities, institutions of higher education, nonprofit organizations, international standards organizations, and Federal agencies, as the Director determines appropriate, including conducting periodic outreach to such entities, institutions, organizations, and agencies.\n**(B)**\nPublish in the Federal Register a draft of the structured template and associated technical guidelines referred to in paragraph (1), and provide an opportunity for submission of public comments for a period of not less than 60 days to be considered for incorporation into such template and guidelines.\n**(4) Reporting and publication**\nNot later than 12 months after the date on which the Director establishes the pilot program pursuant to paragraph (1), the Director shall carry out the following:\n**(A)**\nSubmit to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report that includes the following:\n**(i)**\nAn assessment on the effectiveness of such pilot program.\n**(ii)**\nIf so assessed to be effective, a plan for permanent implementation, including relating to administration, of such pilot program.\n**(B)**\nMake publicly available on the website of the National Institute of Standards and Technology the structured template and associated technical guidelines referred to in paragraph (1), including the incorporation of any appropriate comments in accordance with paragraph (3)(B).\n**(5) Definitions**\nIn this Act:\n**(A) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n**(B) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(C) Artificial intelligence model**\nThe term artificial intelligence model means a software component of an information system that implements artificial intelligence technology and uses computational, statistical, or machine-learning techniques to produce outputs from a defined set of inputs.\n**(D) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1001(a) ).\n**(E) Nonprofit organization**\nThe term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code.\n**(F) International standards organization**\nThe term international standards organization has the meaning given such term in section 451 of the Trade Agreements Act of 1979 ( 19 U.S.C. 2571 ).",
      "versionDate": "2025-12-04",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-05T16:21:46Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6461ih.xml"
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
      "title": "READ AI Models Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "READ AI Models Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Resources for Evaluating and Documenting AI Models",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the National Institute of Standards and Technology to develop best practices and technical guidance on artificial intelligence model documentation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:48:19Z"
    }
  ]
}
```
