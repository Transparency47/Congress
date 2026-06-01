# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3704
- Title: COP Act
- Congress: 119
- Bill type: S
- Bill number: 3704
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-02-20T16:00:09Z
- Update date including text: 2026-02-20T16:00:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3704",
    "number": "3704",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "COP Act",
    "type": "S",
    "updateDate": "2026-02-20T16:00:09Z",
    "updateDateIncludingText": "2026-02-20T16:00:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T22:36:01Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3704is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3704\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mrs. Moody introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit threats to a minor, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Combating Online Predators Act or the COP Act .\n#### 2. Prohibiting threats to a minor\n##### (a) Material involving the sexual exploitation of minors\nSection 2252A of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (6), by striking illegal; or and inserting illegal; ;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting ; or ; and\n**(C)**\nby inserting after paragraph (7) the following:\n(8) knowingly distributes, offers, sends, or provides, in or affecting interstate or foreign commerce, a threat to distribute\u2014 (A) a visual depiction of a minor engaging in sexually explicit conduct, or (B) a visual depiction of a person the defendant believes is a minor engaging in sexually explicit conduct, with the intent that the minor, or the person the defendant believes is a minor, create or transmit a visual depiction of any minor engaging in sexually explicit conduct, ; and\n**(2)**\nin subsection (b), by striking or (6) and inserting (6), or (8) .\n##### (b) Material constituting or containing child pornography\nSection 2252 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3)(B)(ii), by striking or at the end;\n**(B)**\nin paragraph (4)(B)(ii), by inserting or after the semicolon; and\n**(C)**\nby inserting after paragraph (4) the following:\n(5) knowingly distributes, offers, sends, or provides, in or affecting interstate or foreign commerce, a threat to distribute\u2014 (A) a visual depiction of a minor engaging in sexually explicit conduct, or (B) a visual depiction of a person the defendant believes is a minor engaging in sexually explicit conduct, with the intent that the minor, or the person the defendant believes is a minor, create or transmit a visual depiction of sexually explicit conduct, ;\n**(2)**\nin subsection (b)(2), by inserting or (5) after paragraph (4) ; and\n**(3)**\nin subsection (c), in the matter preceding paragraph (1), by inserting or (5) after paragraph (4) .",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-01-13",
        "text": "Received in the Senate and Read twice and referred to the Committee on the Judiciary."
      },
      "number": "6719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Combating Online Predators Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-20T16:00:08Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3704is.xml"
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
      "title": "COP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combating Online Predators Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit threats to a minor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:21Z"
    }
  ]
}
```
