# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/304?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/304
- Title: Birthright Citizenship Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 304
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-17T12:03:15Z
- Update date including text: 2025-12-17T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/304",
    "number": "304",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Birthright Citizenship Act of 2025",
    "type": "S",
    "updateDate": "2025-12-17T12:03:15Z",
    "updateDateIncludingText": "2025-12-17T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T18:35:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TX"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "UT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "OH"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s304is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 304\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Graham (for himself, Mr. Cruz , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 301 of the Immigration and Nationality Act to clarify those classes of individuals born in the United States who are nationals and citizens of the United States at birth.\n#### 1. Short title\nThis Act may be cited as the Birthright Citizenship Act of 2025 .\n#### 2. Citizenship at birth for certain persons born in the United States\n##### (a) In general\nSection 301 of the Immigration and Nationality Act ( 8 U.S.C. 1401 ) is amended\u2014\n**(1)**\nby inserting (a) In general.\u2014 before The following ;\n**(2)**\nby redesignating subsections (a) through (h) as paragraphs (1) through (8), respectively; and\n**(3)**\nby adding at the end the following:\n(b) Definition Acknowledging the right of birthright citizenship established by section 1 of the 14th amendment to the Constitution, a person born in the United States shall be considered \u2018subject to the jurisdiction\u2019 of the United States for purposes of subsection (a)(1) if the person is born in the United States of parents, one of whom is\u2014 (1) a citizen or national of the United States; (2) an alien lawfully admitted for permanent residence in the United States whose residence is in the United States; or (3) an alien in lawful status performing active service in the armed forces (as defined in section 101 of title 10, United States Code). .\n##### (b) Applicability\nThe amendment made by subsection (a)(3) shall not be construed to affect the citizenship or nationality status of any person born before the date of the enactment of this Act.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-21",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "569",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Birthright Citizenship Act of 2025",
      "type": "HR"
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
        "name": "Immigration",
        "updateDate": "2025-03-07T15:55:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s304",
          "measure-number": "304",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-05-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s304v00",
            "update-date": "2025-05-23"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Birthright Citizenship Act of 2025 </strong></p><p>This bill limits birthright citizenship by redefining what it means to be <em>subject to the jurisdiction</em> of the United States.</p><p>Currently, a person born in the United States and subject to U.S. jurisdiction is entitled to citizenship. Under the bill, a person is subject to U.S. jurisdiction if he or she is born to a parent who is (1) a U.S. citizen or national, (2) a lawful permanent resident residing in the United States, or (3) a non-U.S. national (<em>alien </em>under federal law)\u00a0in lawful status who is performing active service in the Armed Forces.</p><p>The bill does not affect the citizenship or nationality status of any person born before the bill's enactment date.</p>"
        },
        "title": "Birthright Citizenship Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s304.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Birthright Citizenship Act of 2025 </strong></p><p>This bill limits birthright citizenship by redefining what it means to be <em>subject to the jurisdiction</em> of the United States.</p><p>Currently, a person born in the United States and subject to U.S. jurisdiction is entitled to citizenship. Under the bill, a person is subject to U.S. jurisdiction if he or she is born to a parent who is (1) a U.S. citizen or national, (2) a lawful permanent resident residing in the United States, or (3) a non-U.S. national (<em>alien </em>under federal law)\u00a0in lawful status who is performing active service in the Armed Forces.</p><p>The bill does not affect the citizenship or nationality status of any person born before the bill's enactment date.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s304"
    },
    "title": "Birthright Citizenship Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Birthright Citizenship Act of 2025 </strong></p><p>This bill limits birthright citizenship by redefining what it means to be <em>subject to the jurisdiction</em> of the United States.</p><p>Currently, a person born in the United States and subject to U.S. jurisdiction is entitled to citizenship. Under the bill, a person is subject to U.S. jurisdiction if he or she is born to a parent who is (1) a U.S. citizen or national, (2) a lawful permanent resident residing in the United States, or (3) a non-U.S. national (<em>alien </em>under federal law)\u00a0in lawful status who is performing active service in the Armed Forces.</p><p>The bill does not affect the citizenship or nationality status of any person born before the bill's enactment date.</p>",
      "updateDate": "2025-05-23",
      "versionCode": "id119s304"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s304is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Birthright Citizenship Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Birthright Citizenship Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 301 of the Immigration and Nationality Act to clarify those classes of individuals born in the United States who are nationals and citizens of the United States at birth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:25Z"
    }
  ]
}
```
