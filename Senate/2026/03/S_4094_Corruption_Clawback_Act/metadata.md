# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4094?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4094
- Title: Corruption Clawback Act
- Congress: 119
- Bill type: S
- Bill number: 4094
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-03-30T22:29:13Z
- Update date including text: 2026-03-30T22:29:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4094",
    "number": "4094",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Corruption Clawback Act",
    "type": "S",
    "updateDate": "2026-03-30T22:29:13Z",
    "updateDateIncludingText": "2026-03-30T22:29:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T18:45:32Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4094is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4094\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Schiff (for himself, Ms. Hirono , Mr. Durbin , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Attorney General to recover certain payments made to the President.\n#### 1. Short title\nThis Act may be cited as the Corruption Clawback Act .\n#### 2. Definition\nIn this Act, the term covered payment means any portion of any monetary settlement, administrative award, including an award made under section 2672 of title 28, United States Code, or a court-ordered judgment\u2014\n**(1)**\npaid from the United States Treasury or in accordance with section 1304 of title 31, United States Code;\n**(2)**\npaid to an individual when they served as President;\n**(3)**\nthat would not have been paid but for the individual holding the status, authority, or duties associated with their position as President; and\n**(4)**\nrelating to an administrative claim filed or settlement reached on or after January 20, 2025.\n#### 3. Recovery of payments made to the President\n##### (a) In general\nThe Attorney General shall bring a civil action in the United States Court of Federal Claims or the United States Court of Appeals for the District of Columbia Circuit to recover any covered payment.\n##### (b) Considerations\nIn determining whether a payment described in section 2 would not have been made but for the individual holding the status, authority, or duties associated with their position as President, the court should consider\u2014\n**(1)**\nwhether the officials who authorized or negotiated the covered payment on behalf of the Government were appointed by, or previously served as personal counsel to, the President;\n**(2)**\nwhether the amount of the covered payment exceeds typical payouts for similar claims by private citizens; and\n**(3)**\nwhether the settlement bypassed standard legal defenses (such as statutes of limitations or sovereign immunity) that career Government lawyers would typically assert.\n##### (c) Use of recovered payments\nAny covered payment that is recovered under this section shall be used by the Public Integrity Section of the Criminal Division of the Department of Justice.\n#### 4. Report\nNot later than 180 days after the date on which a covered payment that is greater than $1,000,000 is made, the Comptroller General shall submit to Congress a report that includes the considerations described in section 3(b).",
      "versionDate": "2026-03-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-30T22:29:12Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4094is.xml"
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
      "title": "Corruption Clawback Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Corruption Clawback Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Attorney General to recover certain payments made to the President.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:23Z"
    }
  ]
}
```
