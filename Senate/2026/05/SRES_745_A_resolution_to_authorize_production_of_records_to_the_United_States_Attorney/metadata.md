# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/745
- Title: A resolution to authorize production of records to the United States Attorney.
- Congress: 119
- Bill type: SRES
- Bill number: 745
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-22T14:59:07Z
- Update date including text: 2026-05-22T14:59:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2026-05-20 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2428; text: CR S2420)
- Latest action: 2026-05-20: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.

## Actions

- 2026-05-20 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2026-05-20 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2428; text: CR S2420)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent."
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/745",
    "number": "745",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "A resolution to authorize production of records to the United States Attorney.",
    "type": "SRES",
    "updateDate": "2026-05-22T14:59:07Z",
    "updateDateIncludingText": "2026-05-22T14:59:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2428; text: CR S2420)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres745ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 745\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Thune (for himself and Mr. Schumer ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nTo authorize production of records to the United States Attorney.\nThat the office of Senator Mark Warner is authorized to produce documents to the United States Attorney, except concerning matters for which a privilege should be asserted.",
      "versionDate": "2026-05-20",
      "versionType": "ATS"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres745ats.xml"
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
      "title": "A resolution to authorize production of records to the United States Attorney.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:28Z"
    },
    {
      "title": "A resolution to authorize production of records to the United States Attorney.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T10:56:28Z"
    }
  ]
}
```
