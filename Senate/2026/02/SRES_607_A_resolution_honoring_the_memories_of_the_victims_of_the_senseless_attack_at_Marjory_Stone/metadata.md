# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/607
- Title: A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.
- Congress: 119
- Bill type: SRES
- Bill number: 607
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-04-03T15:15:25Z
- Update date including text: 2026-04-03T15:15:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S612)
- 2026-02-12 - IntroReferral: Submitted in Senate
- Latest action: 2026-02-12: Submitted in Senate

## Actions

- 2026-02-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S612)
- 2026-02-12 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/607",
    "number": "607",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.",
    "type": "SRES",
    "updateDate": "2026-04-03T15:15:25Z",
    "updateDateIncludingText": "2026-04-03T15:15:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S612)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-02-12T17:35:45Z",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres607is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 607\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Scott of Florida (for himself and Mrs. Moody ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.\nThat the Senate\u2014\n**(1)**\nhonors the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018, and offers heartfelt condolences and deepest sympathies to the families, loved ones, and friends of the victims;\n**(2)**\nhonors the survivors of the attack and pledges continued support for their recovery;\n**(3)**\nrecognizes the strength and resilience of the Marjory Stoneman Douglas High School community; and\n**(4)**\nexpresses gratitude to the emergency medical and health care professionals of the Parkland community for their efforts in responding to the attack and caring for the victims and survivors.",
      "versionDate": "2026-02-12",
      "versionType": "IS"
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
        "actionDate": "2025-02-13",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S990; text: CR S981)"
      },
      "number": "79",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.",
      "type": "SRES"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-18T15:52:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-12",
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
          "measure-id": "id119sres607",
          "measure-number": "607",
          "measure-type": "sres",
          "orig-publish-date": "2026-02-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres607v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution honors the memories of the victims killed in the attack on February 14, 2018, at Marjory Stoneman Douglas High School in Parkland, Florida, and offers condolences to the families, loved ones, and friends of the victims.</p> <p>The resolution (1) honors the survivors and pledges continued support for their recovery, (2) recognizes the strength and resilience of the Marjory Stoneman Douglas High School community, and (3) expresses gratitude to the emergency medical and health care professionals of the Parkland community for their efforts in responding to the attack and caring for the victims and survivors. </p>"
        },
        "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres607.xml",
    "summary": {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors the memories of the victims killed in the attack on February 14, 2018, at Marjory Stoneman Douglas High School in Parkland, Florida, and offers condolences to the families, loved ones, and friends of the victims.</p> <p>The resolution (1) honors the survivors and pledges continued support for their recovery, (2) recognizes the strength and resilience of the Marjory Stoneman Douglas High School community, and (3) expresses gratitude to the emergency medical and health care professionals of the Parkland community for their efforts in responding to the attack and caring for the victims and survivors. </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres607"
    },
    "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018."
  },
  "summaries": [
    {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution honors the memories of the victims killed in the attack on February 14, 2018, at Marjory Stoneman Douglas High School in Parkland, Florida, and offers condolences to the families, loved ones, and friends of the victims.</p> <p>The resolution (1) honors the survivors and pledges continued support for their recovery, (2) recognizes the strength and resilience of the Marjory Stoneman Douglas High School community, and (3) expresses gratitude to the emergency medical and health care professionals of the Parkland community for their efforts in responding to the attack and caring for the victims and survivors. </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres607"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres607is.xml"
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
      "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-14T04:18:24Z"
    },
    {
      "title": "A resolution honoring the memories of the victims of the senseless attack at Marjory Stoneman Douglas High School on February 14, 2018.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:56:30Z"
    }
  ]
}
```
