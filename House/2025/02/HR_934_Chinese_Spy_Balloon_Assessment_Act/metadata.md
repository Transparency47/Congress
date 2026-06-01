# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/934?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/934
- Title: Chinese Spy Balloon Assessment Act
- Congress: 119
- Bill type: HR
- Bill number: 934
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-01-21T01:41:15Z
- Update date including text: 2026-01-21T01:41:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/934",
    "number": "934",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Chinese Spy Balloon Assessment Act",
    "type": "HR",
    "updateDate": "2026-01-21T01:41:15Z",
    "updateDateIncludingText": "2026-01-21T01:41:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WY"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "SC"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr934ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 934\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Fry (for himself, Ms. Hageman , Mr. Webster of Florida , Ms. Malliotakis , Mr. Norman , Mr. Higgins of Louisiana , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to submit a report about the effects on national security of the surveillance conducted by the People\u2019s Republic of China via the high-altitude surveillance balloon shot down in the airspace of the United States in February 2023, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chinese Spy Balloon Assessment Act .\n#### 2. Report on the effects on national security of certain surveillance conducted by the People\u2019s Republic of China\n##### (a) Report\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense, in consultation with the President, shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report about the effects on national security of surveillance conducted by the People\u2019s Republic of China via the high-altitude surveillance balloon shot down in the airspace of the United States in February 2023, including\u2014\n**(1)**\na description of any such effects on military installations; and\n**(2)**\nan analysis of any technology and materials recovered from the high-altitude surveillance balloon, including each country of origin of such technology and materials, if a country of origin can be determined.\n##### (b) Form\nThe report required under this section shall be submitted in an unclassified form, but may include a classified annex.\n##### (c) Military installation defined\nIn this section, the term military installation has the meaning given such term in section 2801 of title 10, United States Code.",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2025-06-13T18:42:10Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2025-06-13T18:42:46Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-13T18:42:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:42:41Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T18:42:21Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-13T18:42:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-05T15:41:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr934",
          "measure-number": "934",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr934v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Chinese Spy Balloon Assessment Act</b></p> <p>This bill requires the Department of Defense to consult with the President and report on the effects on national security of surveillance conducted by China via the high-altitude surveillance balloon shot down in the United States in February 2023. The report must be submitted in an unclassified form, but may include a classified annex.</p>"
        },
        "title": "Chinese Spy Balloon Assessment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr934.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Chinese Spy Balloon Assessment Act</b></p> <p>This bill requires the Department of Defense to consult with the President and report on the effects on national security of surveillance conducted by China via the high-altitude surveillance balloon shot down in the United States in February 2023. The report must be submitted in an unclassified form, but may include a classified annex.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr934"
    },
    "title": "Chinese Spy Balloon Assessment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Chinese Spy Balloon Assessment Act</b></p> <p>This bill requires the Department of Defense to consult with the President and report on the effects on national security of surveillance conducted by China via the high-altitude surveillance balloon shot down in the United States in February 2023. The report must be submitted in an unclassified form, but may include a classified annex.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr934"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr934ih.xml"
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
      "title": "Chinese Spy Balloon Assessment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T10:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chinese Spy Balloon Assessment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to submit a report about the effects on national security of the surveillance conducted by the People's Republic of China via the high-altitude surveillance balloon shot down in the airspace of the United States in February 2023, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T10:03:48Z"
    }
  ]
}
```
