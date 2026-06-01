# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/101
- Title: Expressing support for the designation of February 4, 2025, as "Transit Equity Day".
- Congress: 119
- Bill type: HRES
- Bill number: 101
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-04-16T17:44:31Z
- Update date including text: 2025-04-16T17:44:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-04 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-02-04: Referred to the House Committee on Transportation and Infrastructure.

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-04 - Committee: Referred to the Subcommittee on Highways and Transit.

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
      "text": "Referred to the House Committee on Transportation and Infrastructure."
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/101",
    "number": "101",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Expressing support for the designation of February 4, 2025, as \"Transit Equity Day\".",
    "type": "HRES",
    "updateDate": "2025-04-16T17:44:31Z",
    "updateDateIncludingText": "2025-04-16T17:44:31Z"
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
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
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
          "date": "2025-02-04T17:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-04T22:12:29Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres101ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 101\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mrs. Foushee submitted the following resolution; which was referred to the Committee on Transportation and Infrastructure\nRESOLUTION\nExpressing support for the designation of February 4, 2025, as Transit Equity Day .\nThat the House of Representatives\u2014\n**(1)**\nhonors the life and legacy of Rosa Parks by nationally recognizing Transit Equity Day;\n**(2)**\nencourages the use of public transportation and the continued work to make public transit accessible for all;\n**(3)**\napplauds transit agencies across the country that offer fare-free rides on Transit Equity Day; and\n**(4)**\nrespectfully requests that the Clerk of the House of Representatives transmit an enrolled copy of this resolution to\u2014\n**(A)**\nco-executive directors of the Labor Network for Sustainability, Liz Ratzloff and Joshua Dedmond; and\n**(B)**\nconvener of the National Campaign for Transit Justice, LeeAnn Hall.",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-04-16T17:44:10Z"
          },
          {
            "name": "Public transit",
            "updateDate": "2025-04-16T17:44:02Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-04-16T17:44:21Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-04-16T17:44:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-07T13:58:31Z"
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
          "measure-id": "id119hres101",
          "measure-number": "101",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres101v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors the life and legacy of Rosa Parks by nationally recognizing Transit Equity Day. The resolution also encourages the use of public transportation and the continued work to make public transit accessible for all.</p>"
        },
        "title": "Expressing support for the designation of February 4, 2025, as \"Transit Equity Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres101.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the life and legacy of Rosa Parks by nationally recognizing Transit Equity Day. The resolution also encourages the use of public transportation and the continued work to make public transit accessible for all.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres101"
    },
    "title": "Expressing support for the designation of February 4, 2025, as \"Transit Equity Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the life and legacy of Rosa Parks by nationally recognizing Transit Equity Day. The resolution also encourages the use of public transportation and the continued work to make public transit accessible for all.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres101"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres101ih.xml"
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
      "title": "Expressing support for the designation of February 4, 2025, as \"Transit Equity Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:26Z"
    },
    {
      "title": "Expressing support for the designation of February 4, 2025, as \"Transit Equity Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:05:34Z"
    }
  ]
}
```
