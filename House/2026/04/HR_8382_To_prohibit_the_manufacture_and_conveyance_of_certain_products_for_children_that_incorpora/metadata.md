# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8382
- Title: To prohibit the manufacture and conveyance of certain products for children that incorporate an artificial intelligence chatbot, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8382
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-04-30T08:06:35Z
- Update date including text: 2026-04-30T08:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H3000-3001)
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-21 - IntroReferral: Sponsor introductory remarks on measure. (CR H3000-3001)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8382",
    "number": "8382",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "To prohibit the manufacture and conveyance of certain products for children that incorporate an artificial intelligence chatbot, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:35Z",
    "updateDateIncludingText": "2026-04-30T08:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3000-3001)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8382ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8382\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. Moore of Utah introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the manufacture and conveyance of certain products for children that incorporate an artificial intelligence chatbot, and for other purposes.\n#### 1. Prohibition with respect to certain products for children that incorporate artificial intelligence chatbots\n##### (a) In general\nBeginning on the date that is 180 days after the date of the enactment of this Act, no person may manufacture for sale, import into the United States, sell or otherwise convey to another person, offer to sell or convey to another person, or distribute in commerce in any manner any children\u2019s toy or child care article that incorporates as part of such toy or article an artificial intelligence chatbot.\n##### (b) Enforcement\nA violation of subsection (a) shall be treated as a violation of section 19 of the Consumer Product Safety Act ( 15 U.S.C. 2068 ).\n##### (c) Definitions\nIn this section:\n**(1) Artificial intelligence; machine learning**\nThe terms artificial intelligence and machine learning have the meanings given such terms in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Chatbot**\nThe term chatbot means a technology that uses artificial intelligence or machine learning to engage in interactive conversations with a user of such technology.\n**(3) Child care article; children\u2019s toy**\nThe terms child care article and children\u2019s toy have the meanings given such terms in section 108(g)(1) of the Consumer Product Safety Improvement Act of 2008 ( 15 U.S.C. 2057c(g)(1) ).",
      "versionDate": "2026-04-20",
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
        "name": "Commerce",
        "updateDate": "2026-04-27T22:49:46Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8382ih.xml"
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
      "title": "To prohibit the manufacture and conveyance of certain products for children that incorporate an artificial intelligence chatbot, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:18:22Z"
    },
    {
      "title": "To prohibit the manufacture and conveyance of certain products for children that incorporate an artificial intelligence chatbot, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:05:42Z"
    }
  ]
}
```
