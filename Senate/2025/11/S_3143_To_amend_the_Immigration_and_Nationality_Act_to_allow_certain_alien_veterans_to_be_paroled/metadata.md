# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3143
- Title: HOPE Act
- Congress: 119
- Bill type: S
- Bill number: 3143
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-12-03T12:03:24Z
- Update date including text: 2025-12-03T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3143",
    "number": "3143",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "HOPE Act",
    "type": "S",
    "updateDate": "2025-12-03T12:03:24Z",
    "updateDateIncludingText": "2025-12-03T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T22:02:58Z",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "AZ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "OR"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NJ"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3143is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3143\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Ms. Duckworth (for herself, Mr. Gallego , Mr. Blumenthal , Mr. Wyden , Ms. Hirono , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to allow certain alien veterans to be paroled into the United States to receive health care furnished by the Secretary of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Healthcare Opportunities for Patriots in Exile Act or the HOPE Act .\n#### 2. Parole for certain veterans\nSection 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking subparagraph (B) or and inserting subparagraphs (B) and (C) and ; and\n**(2)**\nby adding at the end the following:\n(D) (i) The Secretary of Homeland Security may parole any alien qualified under clause (ii) into the United States\u2014 (I) at the discretion of the Secretary; (II) on a case-by-case basis; and (III) temporarily under such conditions as the Secretary may prescribe. (ii) To qualify for parole under clause (i) an alien applying for admission to the United States shall\u2014 (I) be a veteran (as defined in section 101 of title 38, United States Code); (II) seek parole to receive health care furnished by the Secretary of Veterans Affairs under chapter 17 of title 38, United States Code; and (III) be outside of the United States pursuant to having been ordered removed or voluntarily departed from the United States under section 240B. (iii) Parole of an alien under clause (i) shall not be regarded as an admission of the alien. (iv) If the Secretary of Homeland Security determines that the purposes of such parole have been served the alien shall forthwith return or be returned to the custody from which the alien was paroled. (v) Parole shall not be available under clause (i) for an alien who is inadmissible due to a criminal conviction\u2014 (I) (aa) for a crime of violence (as defined in section 16(a) of title 18, United States Code), excluding a purely political offense; or (bb) for a crime that endangers the national security of the United States; and (II) for which the alien has served a term of imprisonment of at least 5 years. .",
      "versionDate": "2025-11-06",
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
        "name": "Immigration",
        "updateDate": "2025-11-19T15:00:08Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3143is.xml"
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
      "title": "HOPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthcare Opportunities for Patriots in Exile Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to allow certain alien veterans to be paroled into the United States to receive health care furnished by the Secretary of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:30Z"
    }
  ]
}
```
