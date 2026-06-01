# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2923?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2923
- Title: PAAF Act
- Congress: 119
- Bill type: S
- Bill number: 2923
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2025-12-18T19:10:52Z
- Update date including text: 2025-12-18T19:10:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2923",
    "number": "2923",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "PAAF Act",
    "type": "S",
    "updateDate": "2025-12-18T19:10:52Z",
    "updateDateIncludingText": "2025-12-18T19:10:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T18:02:55Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "ME"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MN"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "IN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2923is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2923\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Ms. Hirono (for herself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide for the automatic acquisition of United States citizenship for certain internationally adopted individuals, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Protect Adoptees and American Families Act or the PAAF Act .\n#### 2. United States citizenship for certain internationally adopted individuals\nSection 320(b) of the Immigration and Nationality Act ( 8 U.S.C. 1431(b) ) is amended to read as follows:\n(b) Adopted children of citizen parent (1) In general Subsection (a) shall apply to a child adopted by a United States citizen parent if the child satisfies the requirements applicable to adopted children under subparagraph (E), (F), or (G) of section 101(b)(1), regardless of the date on which the adoption was finalized. (2) Limited application to certain adopted individuals residing in the united states Notwithstanding section 318, an individual born outside of the United States who was adopted by a United States citizen parent shall automatically become a citizen of the United States when all of the following conditions have been fulfilled: (A) The individual was adopted by a United States citizen before the individual reached 18 years of age. (B) The individual was physically present in the United States in the legal custody of the citizen parent pursuant to a lawful admission before the individual reached 18 years of age. (C) The individual never acquired United States citizenship before the date of the enactment of the Protect Adoptees and American Families Act . (D) The individual was residing in the United States on the date of the enactment of the Protect Adoptees and American Families Act pursuant to a lawful admission. (3) Limited application to certain adopted individuals residing outside of the united states (A) In general Any individual who meets all of the criteria described in subparagraphs (A) through (C) of paragraph (2), but does not meet the requirement described in subparagraph (D) of such paragraph, shall automatically become a citizen of the United States on the date on which the individual is physically present in the United States pursuant to a lawful admission. (B) Inapplicability of grounds of inadmissibility The grounds of inadmissibility set forth in section 212(a) shall not apply to any individual described in subparagraph (A) who is seeking admission to the United States. (C) Criminal background check Notwithstanding subparagraphs (A) and (B), an individual described in subparagraph (A) may not be issued a visa unless\u2014 (i) the individual was subjected to a criminal background check; and (ii) if the background check conducted pursuant to clause (i) reveals that the individual has committed a crime that was not properly resolved, the Secretary of Homeland Security and the Secretary of State coordinated with relevant law enforcement agencies to ensure that appropriate action is taken to resolve such criminal activity. .",
      "versionDate": "2025-09-19",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5492",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PAAF Act",
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
        "updateDate": "2025-12-16T15:48:45Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2923is.xml"
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
      "title": "PAAF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PAAF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Adoptees and American Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the automatic acquisition of United States citizenship for certain internationally adopted individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:21Z"
    }
  ]
}
```
