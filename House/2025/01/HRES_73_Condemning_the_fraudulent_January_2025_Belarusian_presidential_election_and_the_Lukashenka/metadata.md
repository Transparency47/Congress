# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/73?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/73
- Title: Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards.
- Congress: 119
- Bill type: HRES
- Bill number: 73
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-07-01T08:05:42Z
- Update date including text: 2025-07-01T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/73",
    "number": "73",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000375",
        "district": "9",
        "firstName": "William",
        "fullName": "Rep. Keating, William R. [D-MA-9]",
        "lastName": "Keating",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards.",
    "type": "HRES",
    "updateDate": "2025-07-01T08:05:42Z",
    "updateDateIncludingText": "2025-07-01T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:00:35Z",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "SC"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "OH"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "GU"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "DE"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres73ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 73\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Keating (for himself, Mr. Wilson of South Carolina , Ms. Kaptur , and Mr. Smith of New Jersey ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCondemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime\u2019s continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards.\nThat the House of Representatives\u2014\n**(1)**\nstrongly condemns the fraudulent Belarusian presidential elections on January 26, 2025, which were neither free nor fair, and the Lukashenka regime\u2019s continued repression and crackdown against the Belarusian democratic opposition;\n**(2)**\ncalls on the regime to hold free and fair elections with credible international monitoring mechanisms to ensure the voices of the Belarusian people are accurately heard;\n**(3)**\ncondemns the Lukashenka regime\u2019s continued support for Russia\u2019s illegal war of aggression against Ukraine as well as the regime\u2019s complicity in the forcible transfer of Ukrainian children from Ukraine and the use of Belarusian territory as a staging ground for Russian armed forces attacks against Ukraine;\n**(4)**\nsupports additional sanctions against the Lukashenka regime and officials who undermine democracy in Belarus or are complicit in Russia\u2019s war of aggression against Ukraine including judges, police officials, and state-owned businesses that profit on the regime\u2019s repression;\n**(5)**\ncalls for continued support to the Belarusian democratic opposition as well as regular meetings of the Strategic Dialogue between the United States and the Belarusian democratic opposition to demonstrate the United States support for and solidarity with the opposition and as an avenue for pursuing creative solutions to continue to hold the Lukashenka regime accountable for its repression;\n**(6)**\ncalls on the Lukashenka regime to immediately release the more than 1,200 political prisoners who remain behind bars in Belarus;\n**(7)**\nsupports allied and partner governments efforts including sanctions, visa restrictions, and bilateral dialogue mechanisms to hold the Lukashenka regime accountable and support the democratic opposition; and\n**(8)**\nstands with the Belarusian people as they pursue a democratic future free from authoritarian repression.",
      "versionDate": "2025-01-28",
      "versionType": "IH"
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
        "name": "International Affairs",
        "updateDate": "2025-01-31T17:20:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hres73",
          "measure-number": "73",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres73v00",
            "update-date": "2025-03-05"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution condemns the Belarusian presidential election of January 26, 2025, as neither free nor fair and calls on the Lukashenka regime to hold free and fair elections with credible international monitoring. The resolution also condemns the Lukashenka regime's (1) repression of the Belarusian democratic opposition, (2) support for Russia's war against Ukraine, and (3) complicity in the forcible transfer of Ukrainian children from Ukraine.</p><p>The resolution supports additional sanctions against the regime and calls for continued support to the Belarusian democratic opposition. \u00a0</p>"
        },
        "title": "Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres73.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns the Belarusian presidential election of January 26, 2025, as neither free nor fair and calls on the Lukashenka regime to hold free and fair elections with credible international monitoring. The resolution also condemns the Lukashenka regime's (1) repression of the Belarusian democratic opposition, (2) support for Russia's war against Ukraine, and (3) complicity in the forcible transfer of Ukrainian children from Ukraine.</p><p>The resolution supports additional sanctions against the regime and calls for continued support to the Belarusian democratic opposition. \u00a0</p>",
      "updateDate": "2025-03-05",
      "versionCode": "id119hres73"
    },
    "title": "Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution condemns the Belarusian presidential election of January 26, 2025, as neither free nor fair and calls on the Lukashenka regime to hold free and fair elections with credible international monitoring. The resolution also condemns the Lukashenka regime's (1) repression of the Belarusian democratic opposition, (2) support for Russia's war against Ukraine, and (3) complicity in the forcible transfer of Ukrainian children from Ukraine.</p><p>The resolution supports additional sanctions against the regime and calls for continued support to the Belarusian democratic opposition. \u00a0</p>",
      "updateDate": "2025-03-05",
      "versionCode": "id119hres73"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres73ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:20Z"
    },
    {
      "title": "Condemning the fraudulent January 2025 Belarusian presidential election and the Lukashenka regime's continued autocratic rule, calling for continued support for the people of Belarus who seek a democratic future, and calling for free and fair elections in Belarus in line with international standards.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:05:37Z"
    }
  ]
}
```
