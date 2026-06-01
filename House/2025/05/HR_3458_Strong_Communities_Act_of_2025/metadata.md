# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3458
- Title: Strong Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3458
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-05-13T08:06:15Z
- Update date including text: 2026-05-13T08:06:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3458",
    "number": "3458",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Strong Communities Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:15Z",
    "updateDateIncludingText": "2026-05-13T08:06:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "VA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3458ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3458\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Moran (for himself, Ms. Ross , and Mr. Ivey ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide that COPS grant funds may be used for local law enforcement recruits to attend schools or academies if the recruits agree to serve in precincts of law enforcement agencies in their communities.\n#### 1. Short title\nThis Act may be cited as the Strong Communities Act of 2025 .\n#### 2. Strong Communities Program\nSection 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended by adding at the end the following:\n(q) COPS Strong Communities Program (1) Definitions In this subsection: (A) Eligible entity The term eligible entity means\u2014 (i) an institution of higher education, as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ), that, in coordination or through an agreement with a local law enforcement agency, offers a law enforcement training program; or (ii) a local law enforcement agency that offers a law enforcement training program. (B) Local law enforcement agency The term local law enforcement agency means an agency of a State, unit of local government, or Indian Tribe that is authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal law. (2) Grants The Attorney General may use amounts otherwise appropriated to carry out this section for a fiscal year (beginning with fiscal year 2025) to make competitive grants to local law enforcement agencies to be used for officers and recruits to attend law enforcement training programs at eligible entities if the officers and recruits agree to serve in law enforcement agencies in their communities. (3) Eligibility To be eligible for a grant through a local law enforcement agency under this subsection, each officer or recruit described in paragraph (2) shall\u2014 (A) serve as a full-time law enforcement officer for a total of not fewer than 4 years during the 8-year period beginning on the date on which the officer or recruit completes a law enforcement training program for which the officer or recruit receives benefits; (B) complete the service described in subparagraph (A) in a local law enforcement agency located within\u2014 (i) 7 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; or (ii) if the officer or recruit resides in a county with fewer than 150,000 residents, within 20 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; and (C) submit to the eligible entity providing a law enforcement training program to the officer or recruit evidence of employment of the officer or recruit in the form of a certification by the chief administrative officer of the local law enforcement agency where the officer or recruit is employed. (4) Repayment (A) In general If an officer or recruit does not complete the service described in paragraph (3), the officer or recruit shall submit to the local law enforcement agency an amount equal to any benefits the officer or recruit received through the local law enforcement agency under this subsection. (B) Regulations The Attorney General shall promulgate regulations that establish categories of extenuating circumstances under which an officer or recruit may be excused from repayment under subparagraph (A). .\n#### 3. Transparency\nNot less frequently than annually, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that details, with respect to recipients of grants under section 1701(q) of title I of the Omnibus and Crime Control and Safe Streets Act of 1968, as added by section 2\u2014\n**(1)**\nduring the 1-year period preceding the date of the report\u2014\n**(A)**\nthe number and location of those recipients; and\n**(B)**\nthe number of law enforcement officers and recruits each recipient intends to send to law enforcement training programs at eligible entities (as defined in paragraph (1) of such section 1701(q)) with amounts from the grant; and\n**(2)**\nduring the period between the date of enactment of this Act and the date of the report\u2014\n**(A)**\nthe number of law enforcement officers or recruits who attended the training described in paragraph (1)(B) with amounts from the grant and returned from the training as employees of the recipient; and\n**(B)**\nthe number of law enforcement officers or recruits described in subparagraph (A) who remain an employee of the recipient.",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-20",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 82."
      },
      "number": "1316",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strong Communities Act of 2025",
      "type": "S"
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T15:53:43Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-03T15:53:43Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-03T15:53:43Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-03T15:53:43Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-03T15:53:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-28T17:34:48Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3458ih.xml"
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
      "title": "Strong Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strong Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide that COPS grant funds may be used for local law enforcement recruits to attend schools or academies if the recruits agree to serve in precincts of law enforcement agencies in their communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:22Z"
    }
  ]
}
```
