# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/72?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/72
- Title: A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip.
- Congress: 119
- Bill type: SRES
- Bill number: 72
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-03-18T13:31:07Z
- Update date including text: 2025-03-18T13:31:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-03-13 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-03-13 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1751; text: 02/11/2025 CR S863)
- 2025-03-13 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-03-13 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Referred to the Committee on Foreign Relations.
- 2025-03-13 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-03-13 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1751; text: 02/11/2025 CR S863)
- 2025-03-13 - Discharge: Senate Committee on Foreign Relations discharged by Unanimous Consent.
- 2025-03-13 - Committee: Senate Committee on Foreign Relations discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/72",
    "number": "72",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip.",
    "type": "SRES",
    "updateDate": "2025-03-18T13:31:07Z",
    "updateDateIncludingText": "2025-03-18T13:31:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S1751; text: 02/11/2025 CR S863)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Foreign Relations discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
        "item": [
          {
            "date": "2025-03-14T00:11:42Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-02-11T20:24:23Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CT"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NV"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres72is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 72\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Graham (for himself, Mr. Blumenthal , Mr. Cotton , Ms. Rosen , and Mrs. Britt ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nAffirming that Hamas cannot retain any political or military control in the Gaza Strip .\nThat the Senate\u2014\n**(1)**\naffirms that Hamas cannot be allowed to retain any political or military control in the Gaza Strip;\n**(2)**\ncalls upon the President to use all economic and diplomatic tools possible to halt all sources of funding for Hamas from the Islamic Republic of Iran and all other sources of revenue; and\n**(3)**\nsupports the State of Israel as it continues to defend its sovereignty against attacks from Hamas, the Islamic Republic of Iran, and all other Iranian proxies.",
      "versionDate": "2025-02-11",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres72ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 72\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Graham (for himself, Mr. Blumenthal , Mr. Cotton , Ms. Rosen , Mrs. Britt , and Mr. Fetterman ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nMarch 13, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nAffirming that Hamas cannot retain any political or military control in the Gaza Strip .\nThat the Senate\u2014\n**(1)**\naffirms that Hamas cannot be allowed to retain any political or military control in the Gaza Strip;\n**(2)**\ncalls upon the President to use all economic and diplomatic tools possible to halt all sources of funding for Hamas from the Islamic Republic of Iran and all other sources of revenue; and\n**(3)**\nsupports the State of Israel as it continues to defend its sovereignty against attacks from Hamas, the Islamic Republic of Iran, and all other Iranian proxies.",
      "versionDate": "2025-03-13",
      "versionType": "ATS"
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
            "name": "Arab-Israeli relations",
            "updateDate": "2025-03-18T13:27:24Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-03-18T13:27:43Z"
          },
          {
            "name": "Israel",
            "updateDate": "2025-03-18T13:27:49Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-03-18T13:26:48Z"
          },
          {
            "name": "Palestinians",
            "updateDate": "2025-03-18T13:26:59Z"
          },
          {
            "name": "Political parties and affiliation",
            "updateDate": "2025-03-18T13:26:39Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-03-18T13:31:07Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-03-18T13:26:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-21T13:14:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119sres72",
          "measure-number": "72",
          "measure-type": "sres",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres72v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution affirms that Hamas cannot be allowed to retain any political or military control in the Gaza Strip. The resolution also (1) calls on the President to use economic and diplomatic tools to halt funding for Hamas from Iran and elsewhere; and (2) supports Israel as it defends itself from Hamas, Iran, and Iranian proxies.</p>"
        },
        "title": "A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres72.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution affirms that Hamas cannot be allowed to retain any political or military control in the Gaza Strip. The resolution also (1) calls on the President to use economic and diplomatic tools to halt funding for Hamas from Iran and elsewhere; and (2) supports Israel as it defends itself from Hamas, Iran, and Iranian proxies.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119sres72"
    },
    "title": "A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip."
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution affirms that Hamas cannot be allowed to retain any political or military control in the Gaza Strip. The resolution also (1) calls on the President to use economic and diplomatic tools to halt funding for Hamas from Iran and elsewhere; and (2) supports Israel as it defends itself from Hamas, Iran, and Iranian proxies.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119sres72"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres72is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres72ats.xml"
        }
      ],
      "type": "ATS"
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
      "title": "A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T04:18:25Z"
    },
    {
      "title": "A resolution affirming that Hamas cannot retain any political or military control in the Gaza Strip.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:56:22Z"
    }
  ]
}
```
