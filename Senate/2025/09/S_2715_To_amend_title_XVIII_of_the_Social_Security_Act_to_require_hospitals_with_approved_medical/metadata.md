# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2715?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2715
- Title: FAIR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2715
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2025-12-18T12:03:20Z
- Update date including text: 2025-12-18T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2715",
    "number": "2715",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "FAIR Act of 2025",
    "type": "S",
    "updateDate": "2025-12-18T12:03:20Z",
    "updateDateIncludingText": "2025-12-18T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T17:36:10Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NM"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-09-04",
      "state": "ME"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "AL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "AL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "MT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NH"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2715is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2715\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Daines (for himself, Mr. Heinrich , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require hospitals with approved medical residency training programs to submit to the Secretary of Health and Human Services certain information regarding osteopathic and allopathic candidates for such programs.\n#### 1. Short title\nThis Act may be cited as the Fair Access In Residency Act of 2025 or the FAIR Act of 2025 .\n#### 2. Encouraging more equitable treatment of osteopathic and allopathic candidates in residency application and review process\n##### (a) In general\nSection 1886(d)(5)(B) of the Social Security Act ( 42 U.S.C. 1395ww(d)(5)(B) ) is amended\u2014\n**(1)**\nin clause (i), by inserting at the end the following new sentence: For discharges occurring on or after October 1, 2026, the amount determined under the previous sentence for a hospital shall be reduced by 2 percent for each prior fiscal year (beginning with fiscal year 2025) for which the hospital has not submitted to the Secretary the information described in subclause (xiv). ; and\n**(2)**\nby adding at the end the following new clause:\n(xiv) For purposes of clause (i), the information described in this clause is, with respect to a hospital and a fiscal year, the following: (I) The number of applicants for residency in each of the hospital\u2019s approved medical residency training programs beginning in such fiscal year\u2014 (aa) from osteopathic medical schools; and (bb) from allopathic medical schools. (II) The number of such applicants accepted into each such program beginning in such fiscal year from each such type of medical school. (III) An affirmation that\u2014 (aa) the policy of the hospital is to consider for acceptance to each such program applicants from both osteopathic and allopathic medical schools; and (bb) in the case that the hospital requires applicants to submit an examination score as a prerequisite for acceptance in such a program, the hospital accepts scores from, at the election of the applicant, either the Comprehensive Osteopathic Medical Licensing Examination of the United States or the United States Medical Licensing Examination. .\n##### (b) Publication\nThe Secretary of Health and Human Services shall publish on a public website the information described in subclauses (I) and (II) of section 1886(d)(5)(B)(xiv) of the Social Security Act, as added by subsection (a), and the affirmation described in subclause (III) of such section, that is submitted by a hospital with respect to an approved medical residency training program (as defined in section 1886(h)(5)(A) of the Social Security Act ( 42 U.S.C. 1395ww(h)(5)(A) )) for each fiscal year (beginning with fiscal year 2025).\n##### (c) Rule of construction\nNothing in this Act shall be construed as federalizing medical education, or as establishing a mandate for an approved medical residency training program (as defined in section 1886(h)(5)(A) of the Social Security Act ( 42 U.S.C. 1395ww(h)(5)(A) )) to accept students (or to accept a certain number of students) from osteopathic or allopathic medical schools.",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-03-25",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2314",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAIR Act",
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
        "updateDate": "2025-09-23T15:24:10Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2715is.xml"
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
      "title": "FAIR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAIR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Access In Residency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require hospitals with approved medical residency training programs to submit to the Secretary of Health and Human Services certain information regarding osteopathic and allopathic candidates for such programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:20Z"
    }
  ]
}
```
