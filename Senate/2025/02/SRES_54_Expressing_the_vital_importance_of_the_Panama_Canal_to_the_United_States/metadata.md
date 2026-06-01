# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/54?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/54
- Title: A resolution expressing the vital importance of the Panama Canal to the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 54
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-03-10T14:34:36Z
- Update date including text: 2025-03-10T14:34:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S598)
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S598)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/54",
    "number": "54",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A resolution expressing the vital importance of the Panama Canal to the United States.",
    "type": "SRES",
    "updateDate": "2025-03-10T14:34:36Z",
    "updateDateIncludingText": "2025-03-10T14:34:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S598)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-04T21:22:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres54is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 54\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Lee (for himself, Mr. Scott of Florida , Mr. Tuberville , and Mrs. Blackburn ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the vital importance of the Panama Canal to the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes the ingenuity and labor of Americans that made the Panama Canal possible for future generations, with special regard for those Americans who lost their lives in pursuit of the Panama Canal project;\n**(2)**\nexpresses that the Panama Canal is vital to United States regional security, hemispheric hegemony, and economic interests;\n**(3)**\nassesses that a pattern of Chinese-backed investment in port infrastructure and canal operations in Panama constitutes a violation of the Neutrality Treaty; and\n**(4)**\nurges the Trump administration to ensure that the canal remains neutral and to take all appropriate measures to enforce the Neutrality Treaty.",
      "versionDate": "2025-02-04",
      "versionType": "IS"
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
        "updateDate": "2025-02-21T13:07:50Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119sres54",
          "measure-number": "54",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres54v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses that the Panama Canal is vital to U.S. regional security, hemispheric hegemony, and economic interests. The resolution also assesses that Chinese-backed investment in Panama's port infrastructure and canal operations violates the Neutrality Treaty (i.e., the Treaty Concerning the Permanent Neutrality and Operation of the Panama Canal, signed in 1977) and urges the administration to ensure that the canal remains neutral.</p>"
        },
        "title": "A resolution expressing the vital importance of the Panama Canal to the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres54.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses that the Panama Canal is vital to U.S. regional security, hemispheric hegemony, and economic interests. The resolution also assesses that Chinese-backed investment in Panama's port infrastructure and canal operations violates the Neutrality Treaty (i.e., the Treaty Concerning the Permanent Neutrality and Operation of the Panama Canal, signed in 1977) and urges the administration to ensure that the canal remains neutral.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119sres54"
    },
    "title": "A resolution expressing the vital importance of the Panama Canal to the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses that the Panama Canal is vital to U.S. regional security, hemispheric hegemony, and economic interests. The resolution also assesses that Chinese-backed investment in Panama's port infrastructure and canal operations violates the Neutrality Treaty (i.e., the Treaty Concerning the Permanent Neutrality and Operation of the Panama Canal, signed in 1977) and urges the administration to ensure that the canal remains neutral.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119sres54"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres54is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the vital importance of the Panama Canal to the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:22Z"
    },
    {
      "title": "A resolution expressing the vital importance of the Panama Canal to the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T11:56:17Z"
    }
  ]
}
```
