# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4374?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4374
- Title: Airpower Acceleration Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4374
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-13T20:48:44Z
- Update date including text: 2026-05-13T20:48:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-04-22: Introduced in Senate

## Actions

- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4374",
    "number": "4374",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Airpower Acceleration Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T20:48:44Z",
    "updateDateIncludingText": "2026-05-13T20:48:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T18:40:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NH"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-22",
      "state": "ME"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "SD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "ND"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4374is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4374\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Budd (for himself, Mrs. Shaheen , Mr. King , Mr. Schmitt , Mr. Sheehy , Mr. Rounds , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of Defense to enter into multiyear contracts for the procurement of F\u201335 and F\u201315EX aircraft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Airpower Acceleration Act of 2026 .\n#### 2. Multiyear procurement authority for F\u201335 and F\u201315EX aircraft\n##### (a) Multiyear procurement authority\nSubject to section 3501 of title 10, United States Code, except as provided in this section, the Secretary of Defense may enter into one or more multiyear contracts for the procurement of F\u201335A, F\u201335B, F\u201335C, and F\u201315EX aircraft.\n##### (b) Findings requirements\n**(1) In general**\nA contract described in subsection (a) is deemed to meet the requirements of section 3501(a) of such title.\n**(2) Request**\nSection 3501(i)(2) of such title shall not apply for purposes of this Act.\n**(3) Report**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Defense shall submit to Congress a report with respect to contracts described in subsection (a) containing preliminary findings of the agency head described in paragraphs (1) through (6) of section 3501(a) of such title, together with the basis for such findings.\n##### (c) Advance procurement\n**(1) In general**\nThe Secretary of Defense may enter into one or more contracts for advance procurement of key components of F\u201335A, F\u201335B, F\u201335C, and F\u201315EX aircraft in economic order quantities.\n**(2) Certification**\nThe Secretary of Defense shall include in any certification submitted under section 3501(i)(3) of such title a description of the specific components the Secretary intends to procure under the authority provided by paragraph (1).\n##### (d) Sense of Congress\nIt is the sense of Congress that the implementation of section 3501(d) of such title is important to ensuring that all subcontractors, vendors, and suppliers promptly receive funds in order to supercharge the defense industrial base.\n#### 3. Modification of inventory requirements for Air Force fighter aircraft\n##### (a) In general\nSubsection (i) of section 9062 of title 10, United States Code, is amended to read as follows:\n(i) (1) The Secretary of the Air Force shall\u2014 (A) during the period beginning on October 1, 2026, and ending on October 1, 2035, maintain a total aircraft inventory of fighter aircraft of not less than 1,800 aircraft; and (B) maintain a total aircraft inventory of combat-coded fighter aircraft of\u2014 (i) not less than 1,369 aircraft by December 31, 2030; and (ii) not less than 1,558 aircraft by December 31, 2035. (2) In this subsection: (A) The term fighter aircraft \u2014 (i) means an aircraft that\u2014 (I) is designated by a mission design series prefix of F\u2013 or A\u2013; (II) is manned by one or two crewmembers; and (III) executes single-role or multi-role missions, including air-to-air combat, air-to-ground attack, air interdiction, suppression or destruction of enemy air defenses, close air support, strike control and reconnaissance, combat search and rescue support, or airborne forward air control; and (ii) does not include collaborative combat aircraft. (B) The term primary mission aircraft inventory means aircraft assigned to meet the primary aircraft authorization to a unit for the performance of its wartime mission. (C) The term total aircraft inventory of combat-coded fighter aircraft means the total inventory of combat-coded fighter aircraft the Air Force possesses, including in\u2014 (i) the primary mission aircraft inventory; (ii) the backup aircraft inventory; and (iii) the attrition reserve. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on October 1, 2026.\n#### 4. F\u201315EX aircraft fleet\n##### (a) Authority\nSubject to subsection (b), the Secretary of the Air Force may increase the size of the F\u201315EX aircraft fleet from 129 to 329 F\u201315EX aircraft.\n##### (b) Condition\nThe Secretary of the Air Force shall use any F\u201315EX aircraft procured after the first 129 aircraft under the authority provided by subsection (a) exclusively for the purpose of recapitalizing the F\u201315E aircraft fleet of the Air Force.",
      "versionDate": "2026-04-22",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-13T20:48:44Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4374is.xml"
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
      "title": "Airpower Acceleration Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T11:03:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Airpower Acceleration Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Defense to enter into multiyear contracts for the procurement of F-35 and F-15EX aircraft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:34Z"
    }
  ]
}
```
