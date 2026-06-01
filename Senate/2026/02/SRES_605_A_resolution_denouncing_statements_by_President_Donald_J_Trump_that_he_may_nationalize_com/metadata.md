# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/605
- Title: A resolution denouncing statements by President Donald J. Trump that he may "nationalize," commandeer, or otherwise assume direct control over elections.
- Congress: 119
- Bill type: SRES
- Bill number: 605
- Origin chamber: Senate
- Introduced date: 2026-02-11
- Update date: 2026-04-27T22:50:33Z
- Update date including text: 2026-04-27T22:50:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in Senate
- 2026-02-11 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S581-582)
- 2026-02-11 - IntroReferral: Submitted in Senate
- Latest action: 2026-02-11: Submitted in Senate

## Actions

- 2026-02-11 - IntroReferral: Referred to the Committee on Rules and Administration. (text: CR S581-582)
- 2026-02-11 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/605",
    "number": "605",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A resolution denouncing statements by President Donald J. Trump that he may \"nationalize,\" commandeer, or otherwise assume direct control over elections.",
    "type": "SRES",
    "updateDate": "2026-04-27T22:50:33Z",
    "updateDateIncludingText": "2026-04-27T22:50:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Rules and Administration. (text: CR S581-582)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
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
          "date": "2026-02-11T23:48:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "sponsorshipDate": "2026-02-11",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres605is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 605\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2026 Mr. Markey (for himself, Mr. Blumenthal , and Mr. Schiff ) submitted the following resolution; which was referred to the Committee on Rules and Administration\nRESOLUTION\nDenouncing statements by President Donald J. Trump that he may nationalize, commandeer, or otherwise assume direct control over elections.\nThat the Senate\u2014\n**(1)**\nfinds that the Constitution of the United States entrusts the primary oversight and administration of Federal elections to State and local authorities and Congress;\n**(2)**\nrejects any suggestion that the President of the United States may lawfully nationalize, commandeer, or otherwise assume direct control over elections;\n**(3)**\nrenounces any effort by the President to exercise such authority, absent explicit constitutional or statutory grant, as antithetical to the Constitution, unlawful, and without effect;\n**(4)**\nexpresses its grave concern that public advocacy of unconstitutional power by the President undermines foundational principles of federalism, threatens the rule of law, and erodes public trust in the democratic process; and\n**(5)**\nmaintains that should the President attempt to implement or execute measures that unconstitutionally infringe on the constitutional prerogatives of the States or contrary to the laws enacted by Congress, such conduct would constitute grounds for impeachment and removal from office under article II of the Constitution.",
      "versionDate": "2026-02-11",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1062",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Denouncing statements by President Donald J. Trump that he may \"nationalize,\" commandeer, or otherwise assume direct control over elections.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-17T18:07:15Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres605is.xml"
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
      "title": "A resolution denouncing statements by President Donald J. Trump that he may \"nationalize,\" commandeer, or otherwise assume direct control over elections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-13T04:03:33Z"
    },
    {
      "title": "A resolution denouncing statements by President Donald J. Trump that he may \"nationalize,\" commandeer, or otherwise assume direct control over elections.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T11:56:27Z"
    }
  ]
}
```
