# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1391?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1391
- Title: Student Veteran Benefit Restoration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1391
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2026-05-21T08:08:26Z
- Update date including text: 2026-05-21T08:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1391",
    "number": "1391",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Student Veteran Benefit Restoration Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:26Z",
    "updateDateIncludingText": "2026-05-21T08:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
        "item": [
          {
            "date": "2026-05-20T13:28:06Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:46:46Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-14T18:31:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "IL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "FL"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "AZ"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1391ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1391\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mrs. Ramirez (for herself, Mr. Takano , Mr. Levin , Ms. Schakowsky , Ms. Budzinski , Mr. Garc\u00eda of Illinois , Mr. Frost , and Mr. Grijalva ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide restoration of entitlement to educational assistance to individuals defrauded by educational institutions receiving payment on behalf of such individuals under the laws administered by the Secretary of Veterans Affairs and to provide repayment of funds to the Secretary from such educational institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Student Veteran Benefit Restoration Act of 2025 .\n#### 2. Requirements for educational institutions that receive educational assistance from programs administered by the Secretary of Veterans Affairs\n##### (a) In general\nSubchapter III of chapter 36 of title 38, United States Code, is amended by adding at the end the following new section:\n3699C. Restoration of entitlement for pursuit of courses or programs of education at certain educational institutions (a) Restoration of entitlement The Secretary shall determine that any payment of covered educational assistance for the pursuit by a covered individual of a course or program of education at an educational institution occurring during a period set forth under subsection (b) is not\u2014 (1) charged against any entitlement of the covered individual to the covered educational assistance; or (2) counted against the aggregate period for which section 3695 of this title limits the receipt of educational assistance by the covered individual. (b) Covered periods A period set forth under this subsection with respect to a course or program of education pursued by a covered individual at an educational institution is any of the following: (1) Any period, occurring on or after the date of enactment of the Student Veteran Benefit Restoration Act of 2025 , in which the educational institution was not approved by a State approving agency or the Secretary acting as a State approving agency, including periods in which an educational institution is not approved because an approval is revoked. (2) Any period, occurring on or after the date of enactment of the Student Veteran Benefit Restoration Act of 2025 , with regards to which the Secretary has made a final determination that the educational institution, or the owner of the educational institution, was in violation during such period of an applicable provision of section 3696 of this title. (3) Any period, occurring on or after the date of enactment of the Student Veteran Benefit Restoration Act of 2025 , during which a court of competent jurisdiction found the educational institution guilty of, or liable for, fraud. (4) Any period, occurring on or after the date of enactment of the Student Veteran Benefit Restoration Act of 2025 , during which the educational institution was closed by the Department of Justice on the basis of fraud or a violation of a provision of Federal or State law. (5) Any period occurring on or after the date of enactment of the Student Veteran Benefit Restoration Act of 2025 \u2014 (A) during which the educational institution engaged in fraud; and (B) after which the educational institution closes. (c) Repayment of funds (1) As a condition of the approval of a course or program of education under this chapter, the educational institution offering the course or program shall agree that if the educational institution receives payment of covered educational assistance for a covered individual to pursue a course or program of education at the educational institution and the Secretary, pursuant to subsection (a), restores to such covered individual some portion of the entitlement of the covered individual to such covered educational assistance, the educational institution shall repay to the Secretary the amount of that portion of the covered educational assistance that the educational institution received for that individual. (2) In the case of an educational institution that has been found guilty of, or liable for, fraud by a court of competent jurisdiction and is ordered to pay financial relief to the Federal Government, the Secretary may file a claim with the Department of the Treasury for recoupment of all amounts of educational assistance received by such educational institution pursuant to the educational assistance programs administered by the Secretary that the Secretary determines were obtained through such fraud. (d) Appeals (1) The Secretary shall establish a process by which an educational institution or the owner of an educational institution that is subject to a finding by the Secretary that the educational institution is required to repay an amount under subsection (c) may request a review of such finding. (2) The process established pursuant to paragraph (1) shall be distinct and separate from the process established under section 3696(i) of this title. (e) Definitions In this section: (1) The term covered educational assistance means educational assistance under chapter 30, 31, 32, 33, or 35 of this title, or chapter 1606 or 1607 of title 10. (2) The term covered individual means a veteran or other individual using covered educational assistance to pursue a course or program of education that has been approved under this chapter. (3) The term fraud means fraud or another false, misleading, or deceptive act or omission. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 3699B the following new item:\n3699C. Restoration of entitlement for pursuit of courses or programs of education at certain educational institutions. .",
      "versionDate": "2025-02-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Education programs funding",
            "updateDate": "2025-07-08T13:01:09Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-07-08T13:01:03Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-07-08T13:00:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:44:39Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1391ih.xml"
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
      "title": "Student Veteran Benefit Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Student Veteran Benefit Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide restoration of entitlement to educational assistance to individuals defrauded by educational institutions receiving payment on behalf of such individuals under the laws administered by the Secretary of Veterans Affairs and to provide repayment of funds to the Secretary from such educational institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:55Z"
    }
  ]
}
```
