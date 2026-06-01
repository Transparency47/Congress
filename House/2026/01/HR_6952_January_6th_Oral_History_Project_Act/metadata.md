# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6952
- Title: January 6th Oral History Project Act
- Congress: 119
- Bill type: HR
- Bill number: 6952
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-01-22T16:00:39Z
- Update date including text: 2026-01-22T16:00:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6952",
    "number": "6952",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "January 6th Oral History Project Act",
    "type": "HR",
    "updateDate": "2026-01-22T16:00:39Z",
    "updateDateIncludingText": "2026-01-22T16:00:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-01-06T23:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6952ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6952\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Mrs. Torres of California (for herself, Ms. Kelly of Illinois , Ms. Friedman , and Mrs. Fletcher ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the American Folklife Center at the Library of Congress to establish an oral history program to collect certain video and audio recordings of personal histories and testimonials and written materials with respect to individuals who were affected by the events at the United States Capitol on January 6, 2021, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the January 6th Oral History Project Act .\n#### 2. Establishment of program at American Folklife Center to collect video and audio recordings of histories of the insurrection attempt of January 6th 2021\n##### (a) In general\nThe Director of the American Folklife Center at the Library of Congress shall establish an oral history program to\u2014\n**(1)**\ncollect video and audio recordings of personal histories and testimonials of individuals who were present at or affected by the events at the United States Capitol on January 6, 2021, including but not limited to Members of Congress, congressional staff, Capitol Police officers, other law enforcement personnel, journalists, and other witnesses;\n**(2)**\ncreate a collection of the recordings obtained (including a catalog and index) which will be available for public use through the National Digital Library of the Library of Congress and such other methods as the Director considers appropriate to the extent feasible subject to available resources; and\n**(3)**\nsolicit, reproduce, and collect written materials (such as contemporaneous notes, text messages, emails, social media posts, photographs, and other documentation) relevant to the personal histories of individuals who experienced or witnessed the events of January 6, 2021, and to catalog such materials in a manner the Director considers appropriate, consistent with and complementary to the efforts described in paragraphs (1) and (2).\n##### (b) Use of and consultation with other entities\nThe Director may carry out the activities described in paragraphs (1) and (3) of subsection (a) through agreements and partnerships entered into with other government and private entities, and may otherwise consult with interested persons (within the limits of available resources) and develop appropriate guidelines and arrangements for soliciting, acquiring, and making available recordings under the program under this Act.\n##### (c) Timing\nAs soon as practicable after the date of the enactment of this Act, the Director shall begin collecting video and audio recordings under subsection (a)(1) and shall prioritize the collection of testimonials from individuals whose accounts may be most at risk of being lost to time or whose perspectives are essential to understanding the full scope of the January 6, 2021, events.\n#### 3. Private support\n##### (a) Acceptance of donations\nThe Librarian of Congress may solicit and accept donations of funds and in-kind contributions to carry out the January 6th oral history program under section 2.\n##### (b) Establishment of separate gift account\nThere is established in the Treasury (among the accounts of the Library of Congress) a gift account for the January 6th oral history program under section 2.\n##### (c) Dedication of funds\nNotwithstanding any other provision of law\u2014\n**(1)**\nany funds donated to the Librarian of Congress to carry out the January 6th oral history program under section 2 shall be deposited entirely into the gift account established under subsection (b);\n**(2)**\nthe funds contained in such account shall be used solely to carry out the January 6th oral history program under section 2; and\n**(3)**\nthe Librarian of Congress may not deposit into such account any funds donated to the Librarian which are not donated for the exclusive purpose of carrying out the January 6th oral history program under section 2.\n#### 4. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act\u2014\n**(1)**\n$500,000 for fiscal year 2027; and\n**(2)**\nsuch sums as may be necessary for each succeeding fiscal year.",
      "versionDate": "2026-01-06",
      "versionType": "Introduced in House"
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
        "name": "Congress",
        "updateDate": "2026-01-22T16:00:38Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6952ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "January 6th Oral History Project Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "January 6th Oral History Project Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the American Folklife Center at the Library of Congress to establish an oral history program to collect certain video and audio recordings of personal histories and testimonials and written materials with respect to individuals who were affected by the events at the United States Capitol on January 6, 2021, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:23Z"
    }
  ]
}
```
