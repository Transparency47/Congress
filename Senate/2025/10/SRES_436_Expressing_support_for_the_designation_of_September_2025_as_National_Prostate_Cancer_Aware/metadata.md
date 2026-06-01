# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/436?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/436
- Title: A resolution expressing support for the designation of September 2025 as "National Prostate Cancer Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 436
- Origin chamber: Senate
- Introduced date: 2025-10-06
- Update date: 2025-12-05T21:31:42Z
- Update date including text: 2025-12-05T21:31:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-06: Introduced in Senate
- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6958-6959)
- Latest action: 2025-10-06: Introduced in Senate

## Actions

- 2025-10-06 - IntroReferral: Introduced in Senate
- 2025-10-06 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-10-06 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6958-6959)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/436",
    "number": "436",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A resolution expressing support for the designation of September 2025 as \"National Prostate Cancer Awareness Month\".",
    "type": "SRES",
    "updateDate": "2025-12-05T21:31:42Z",
    "updateDateIncludingText": "2025-12-05T21:31:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S6959; text: CR S6958-6959)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-06",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "ID"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres436ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 436\nIN THE SENATE OF THE UNITED STATES\nOctober 6, 2025 Mr. Crapo (for himself, Mr. Booker , Mr. Risch , and Mr. Van Hollen ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nExpressing support for the designation of September 2025 as National Prostate Cancer Awareness Month .\nThat the Senate\u2014\n**(1)**\nexpresses support for the designation of National Prostate Cancer Awareness Month ;\n**(2)**\ndeclares that steps should be taken\u2014\n**(A)**\nto raise awareness about the importance of screening methods for, and treatment of, prostate cancer;\n**(B)**\nto encourage research\u2014\n**(i)**\nto improve screening and treatment for prostate cancer;\n**(ii)**\nto discover the causes of prostate cancer; and\n**(iii)**\nto develop a cure for prostate cancer; and\n**(C)**\nto continue to consider ways to improve access to, and the quality of, health care services for detecting and treating prostate cancer; and\n**(3)**\ncalls on the people of the United States, interest groups, and affected persons\u2014\n**(A)**\nto promote awareness of prostate cancer;\n**(B)**\nto take an active role in the fight to end the devastating effects of prostate cancer on individuals, families, and the economy; and\n**(C)**\nto observe National Prostate Cancer Awareness Month with appropriate ceremonies and activities.",
      "versionDate": "2025-10-06",
      "versionType": "ATS"
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
        "actionDate": "2025-09-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "675",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of September 2025 as \"National Prostate Cancer Awareness Month\".",
      "type": "HRES"
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
            "name": "Cancer",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-11-18T19:27:53Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-11-18T19:27:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-11-17T17:22:40Z"
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
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres436ats.xml"
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
      "title": "A resolution expressing support for the designation of September 2025 as \"National Prostate Cancer Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T10:56:16Z"
    },
    {
      "title": "A resolution expressing support for the designation of September 2025 as \"National Prostate Cancer Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T10:56:16Z"
    }
  ]
}
```
