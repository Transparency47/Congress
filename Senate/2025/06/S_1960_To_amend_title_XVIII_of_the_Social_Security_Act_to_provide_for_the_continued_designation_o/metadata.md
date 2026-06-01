# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1960?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1960
- Title: PEAKS Act
- Congress: 119
- Bill type: S
- Bill number: 1960
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-07-24T18:56:47Z
- Update date including text: 2025-07-24T18:56:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1960",
    "number": "1960",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "PEAKS Act",
    "type": "S",
    "updateDate": "2025-07-24T18:56:47Z",
    "updateDateIncludingText": "2025-07-24T18:56:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:46:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WV"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CA"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1960is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1960\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mrs. Capito (for herself, Mr. Padilla , Mr. Justice , Mr. Schiff , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for the continued designation of hospitals that met mountainous terrain or secondary roads distance requirement as critical access hospitals and to modify distance requirements for ambulance services furnished by critical access hospitals.\n#### 1. Short title\nThis Act may be cited as the Preserving Emergency Access in Key Sites Act or the PEAKS Act .\n#### 2. Treatment of hospitals that met mountainous terrain or secondary roads distance requirement for designation as critical access hospital\nSection 1820(h) of the Social Security Act ( 42 U.S.C. 1395i\u20134(h) ) is amended by adding at the end the following new paragraph:\n(4) Treatment of hospitals that met mountainous terrain or secondary roads distance requirement for designation (A) In general In the case of a hospital described in subparagraph (B), the hospital shall be deemed to meet the 15-mile distance requirement for mountainous terrain or secondary roads described in subsection (c)(2)(B)(i)(I) on or after January 1, 2026. (B) Hospital described A hospital described in this subparagraph is a hospital that\u2014 (i) as of the date of enactment of this paragraph, is designated as a critical access hospital; (ii) demonstrates (in a manner determined by the Secretary) that the hospital met the 15-mile distance requirement for mountainous terrain or secondary roads described in subsection (c)(2)(B)(i)(I) as of the hospital's last certification as a critical access hospital; and (iii) after such date of enactment, has a new hospital or other facility described in this subsection located within 10\u201315 miles of the hospital. (C) Regulations Not later than 1 year after the date of enactment of this paragraph, the Secretary shall promulgate regulations to carry out this paragraph. .\n#### 3. Modification of distance requirements for ambulance services furnished by critical access hospitals\nSection 1834(l)(8) of the Social Security Act ( 42 U.S.C. 1395m(l)(8) ) is amended, in the flush matter following subparagraph (B), by inserting (or, for such services furnished on or after January 1, 2026, in the case of mountainous terrain or in areas with only secondary roads available, a 15-mile drive) after 35-mile drive .",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-05",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3778",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PEAKS Act",
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
        "name": "Health",
        "updateDate": "2025-06-26T13:19:01Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1960is.xml"
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
      "title": "PEAKS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PEAKS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preserving Emergency Access in Key Sites Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for the continued designation of hospitals that met mountainous terrain or secondary roads distance requirement as critical access hospitals and to modify distance requirements for ambulance services furnished by critical access hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T05:33:21Z"
    }
  ]
}
```
