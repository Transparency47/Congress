# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2166?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2166
- Title: Head Start for Our Future Act
- Congress: 119
- Bill type: S
- Bill number: 2166
- Origin chamber: Senate
- Introduced date: 2025-06-25
- Update date: 2025-12-11T12:03:16Z
- Update date including text: 2025-12-11T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in Senate
- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-25: Introduced in Senate

## Actions

- 2025-06-25 - IntroReferral: Introduced in Senate
- 2025-06-25 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2166",
    "number": "2166",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Head Start for Our Future Act",
    "type": "S",
    "updateDate": "2025-12-11T12:03:16Z",
    "updateDateIncludingText": "2025-12-11T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T21:32:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sponsorshipDate": "2025-06-25",
      "state": "ME"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "VA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "AZ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-10-20",
      "state": "NJ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2166is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2166\nIN THE SENATE OF THE UNITED STATES\nJune 25 (legislative day, June 24), 2025 Mrs. Gillibrand (for herself, Ms. Collins , Mr. Padilla , Mr. Kaine , Mr. Van Hollen , Mr. Kelly , Mr. Luj\u00e1n , Mrs. Shaheen , Ms. Klobuchar , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to include child development and early learning as community services under the Federal work-study program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Head Start for Our Future Act .\n#### 2. Child development and early learning community services through Federal work-study programs\n##### (a) In general\nSection 441(c)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1087\u201351(c)(1) ) is amended by striking literacy training and inserting child development and early learning (including Head Start programs and Early Head Start programs carried out under the Head Start Act ( 42 U.S.C. 9831 et seq. )), literacy training .\n##### (b) Agreement requirements\nSection 443(b) of the Higher Education Act of 1965 ( 20 U.S.C. 1087\u201353(b) ) is amended\u2014\n**(1)**\nin paragraph (10), by striking and after the semicolon;\n**(2)**\nby redesignating paragraph (11) as paragraph (12); and\n**(3)**\nby adding at the end the following:\n(11) provide assurances that any Head Start program, including an Early Head Start program, employing students through a work-study program under this part will comply with the requirements of sections 645A(j) and 648A(h), respectively, of the Head Start Act ( 42 U.S.C. 9840a(j) , 9843a(h)); and .\n#### 3. Head Start and Early Head Start requirements\n##### (a) Early Head Start\nSection 645A of the Head Start Act ( 42 U.S.C. 9840a ) is amended by adding at the end the following:\n(j) Students in work-Study programs In the case of a student serving an Early Head Start program through a work-study program under section 441(c)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1087\u201351(c)(1) )\u2014 (1) before the Early Head Start agency involved employs the student, the agency shall comply with the requirements of section 648A(g)(3); (2) the student shall comply with all personnel policies applicable to the Early Head Start program under the Head Start program performance standards issued under this subchapter; and (3) the student shall serve the Early Head Start program as an additional paid staff member but\u2014 (A) shall not be left alone with any child through the program, meaning that a paid staff member (not in such a work-study program) shall attend when the student so serves; and (B) shall not count toward the staff included in any staff-to-child ratio applicable to the Early Head Start program under this subchapter. .\n##### (b) Head Start\nSection 648A of the Head Start Act ( 42 U.S.C. 9843a ) is amended by adding at the end the following:\n(h) Students in work-Study programs In the case of a student serving a Head Start program (not an Early Head Start program) through a work-study program under section 441(c)(1) of the Higher Education Act of 1965 ( 20 U.S.C. 1087\u201351(c)(1) )\u2014 (1) before the Head Start agency involved employs the student, the agency shall comply with the requirements of subsection (g)(3); (2) the student shall comply with all personnel policies applicable to the Head Start program under the Head Start program performance standards issued under this subchapter; and (3) the student shall serve the Head Start program as an additional paid staff member but\u2014 (A) shall not be left alone with any child through the program, meaning that a paid staff member (not in such a work-study program) shall attend when the student so serves; and (B) shall not count toward the staff included in any staff-to-child ratio applicable to the Head Start program under this subchapter. .",
      "versionDate": "2025-06-25",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "4318",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Head Start for Our Future Act",
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
        "name": "Education",
        "updateDate": "2025-07-15T10:48:21Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2166is.xml"
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
      "title": "Head Start for Our Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Head Start for Our Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to include child development and early learning as community services under the Federal work-study program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:21Z"
    }
  ]
}
```
