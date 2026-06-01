# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1316
- Title: Strong Communities Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1316
- Origin chamber: Senate
- Introduced date: 2025-04-07
- Update date: 2025-12-05T21:41:25Z
- Update date including text: 2025-12-05T21:41:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in Senate
- 2025-04-07 - IntroReferral: Introduced in Senate
- 2025-04-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 82.
- Latest action: 2025-04-07: Introduced in Senate

## Actions

- 2025-04-07 - IntroReferral: Introduced in Senate
- 2025-04-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-05-15 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment favorably.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-05-20 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.
- 2025-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 82.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1316",
    "number": "1316",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Strong Communities Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:41:25Z",
    "updateDateIncludingText": "2025-12-05T21:41:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 82.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-07",
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
      "actionDate": "2025-04-07",
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
        "item": [
          {
            "date": "2025-05-20T20:16:56Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-15T17:30:08Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-07T22:09:35Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "DE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NC"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "HI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "FL"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "NV"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NH"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1316is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1316\nIN THE SENATE OF THE UNITED STATES\nApril 7, 2025 Mr. Peters (for himself, Mr. Cornyn , Ms. Klobuchar , Mr. Cruz , Mr. Coons , Mr. Tillis , Mr. Padilla , Mrs. Blackburn , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide that COPS grant funds may be used for local law enforcement recruits to attend schools or academies if the recruits agree to serve in precincts of law enforcement agencies in their communities.\n#### 1. Short title\nThis Act may be cited as the Strong Communities Act of 2025 .\n#### 2. Strong Communities Program\nSection 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended by adding at the end the following:\n(q) COPS Strong Communities Program (1) Definitions In this subsection: (A) Eligible entity The term eligible entity means\u2014 (i) an institution of higher education, as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ), that, in coordination or through an agreement with a local law enforcement agency, offers a law enforcement training program; or (ii) a local law enforcement agency that offers a law enforcement training program. (B) Local law enforcement agency The term local law enforcement agency means an agency of a State, unit of local government, or Indian Tribe that is authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal law. (2) Grants The Attorney General may use amounts otherwise appropriated to carry out this section for a fiscal year (beginning with fiscal year 2025) to make competitive grants to local law enforcement agencies to be used for officers and recruits to attend law enforcement training programs at eligible entities if the officers and recruits agree to serve in law enforcement agencies in their communities. (3) Eligibility To be eligible for a grant through a local law enforcement agency under this subsection, each officer or recruit described in paragraph (2) shall\u2014 (A) serve as a full-time law enforcement officer for a total of not fewer than 4 years during the 8-year period beginning on the date on which the officer or recruit completes a law enforcement training program for which the officer or recruit receives benefits; (B) complete the service described in subparagraph (A) in a local law enforcement agency located within\u2014 (i) 7 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; or (ii) if the officer or recruit resides in a county with fewer than 150,000 residents, within 20 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; and (C) submit to the eligible entity providing a law enforcement training program to the officer or recruit evidence of employment of the officer or recruit in the form of a certification by the chief administrative officer of the local law enforcement agency where the officer or recruit is employed. (4) Repayment (A) In general If an officer or recruit does not complete the service described in paragraph (3), the officer or recruit shall submit to the local law enforcement agency an amount equal to any benefits the officer or recruit received through the local law enforcement agency under this subsection. (B) Regulations The Attorney General shall promulgate regulations that establish categories of extenuating circumstances under which an officer or recruit may be excused from repayment under subparagraph (A). .\n#### 3. Transparency\nNot less frequently than annually, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that details, with respect to recipients of grants under section 1701(q) of title I of the Omnibus and Crime Control and Safe Streets Act of 1968, as added by section 2\u2014\n**(1)**\nduring the 1-year period preceding the date of the report\u2014\n**(A)**\nthe number and location of those recipients; and\n**(B)**\nthe number of law enforcement officers and recruits each recipient intends to send to law enforcement training programs at eligible entities (as defined in paragraph (1) of such section 1701(q)) with amounts from the grant; and\n**(2)**\nduring the period between the date of enactment of this Act and the date of the report\u2014\n**(A)**\nthe number of law enforcement officers or recruits who attended the training described in paragraph (1)(B) with amounts from the grant and returned from the training as employees of the recipient; and\n**(B)**\nthe number of law enforcement officers or recruits described in subparagraph (A) who remain an employee of the recipient.",
      "versionDate": "2025-04-07",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1316rs.xml",
      "text": "II\nCalendar No. 82\n119th CONGRESS\n1st Session\nS. 1316\nIN THE SENATE OF THE UNITED STATES\nApril 7, 2025 Mr. Peters (for himself, Mr. Cornyn , Ms. Klobuchar , Mr. Cruz , Mr. Coons , Mr. Tillis , Mr. Padilla , Mrs. Blackburn , Mr. Welch , Mr. Durbin , Mr. Ossoff , Ms. Hirono , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 20, 2025 Reported by Mr. Grassley , with an amendment Omit the part struck through\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide that COPS grant funds may be used for local law enforcement recruits to attend schools or academies if the recruits agree to serve in precincts of law enforcement agencies in their communities.\n#### 1. Short title\nThis Act may be cited as the Strong Communities Act of 2025 .\n#### 2. Strong Communities Program\nSection 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended by adding at the end the following:\n(q) COPS Strong Communities Program (1) Definitions In this subsection: (A) Eligible entity The term eligible entity means\u2014 (i) an institution of higher education, as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ), that, in coordination or through an agreement with a local law enforcement agency, offers a law enforcement training program; or (ii) a local law enforcement agency that offers a law enforcement training program. (B) Local law enforcement agency The term local law enforcement agency means an agency of a State, unit of local government, or Indian Tribe that is authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal law. (2) Grants The Attorney General may use amounts otherwise appropriated to carry out this section for a fiscal year (beginning with fiscal year 2025) to make competitive grants to local law enforcement agencies to be used for officers and recruits to attend law enforcement training programs at eligible entities if the officers and recruits agree to serve in law enforcement agencies in their communities. (3) Eligibility To be eligible for a grant through a local law enforcement agency under this subsection, each officer or recruit described in paragraph (2) shall\u2014 (A) serve as a full-time law enforcement officer for a total of not fewer than 4 years during the 8-year period beginning on the date on which the officer or recruit completes a law enforcement training program for which the officer or recruit receives benefits; (B) complete the service described in subparagraph (A) in a local law enforcement agency located within\u2014 (i) 7 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; or (ii) if the officer or recruit resides in a county with fewer than 150,000 residents, within 20 miles of the residence of the officer or recruit where the officer or recruit has resided for not fewer than 5 years; and (C) submit to the eligible entity providing a law enforcement training program to the officer or recruit evidence of employment of the officer or recruit in the form of a certification by the chief administrative officer of the local law enforcement agency where the officer or recruit is employed. (4) Repayment (A) In general If an officer or recruit does not complete the service described in paragraph (3), the officer or recruit shall submit to the local law enforcement agency an amount equal to any benefits the officer or recruit received through the local law enforcement agency under this subsection. (B) Regulations The Attorney General shall promulgate regulations that establish categories of extenuating circumstances under which an officer or recruit may be excused from repayment under subparagraph (A). .\n#### 3. Transparency\nNot less frequently than annually, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that details, with respect to recipients of grants under section 1701(q) of title I of the Omnibus and Crime Control and Safe Streets Act of 1968, as added by section 2\u2014\n**(1)**\nduring the 1-year period preceding the date of the report\u2014\n**(A)**\nthe number and location of those recipients; and\n**(B)**\nthe number of law enforcement officers and recruits each recipient intends to send to law enforcement training programs at eligible entities (as defined in paragraph (1) of such section 1701(q)) with amounts from the grant; and\n**(2)**\nduring the period between the date of enactment of this Act and the date of the report\u2014\n**(A)**\nthe number of law enforcement officers or recruits who attended the training described in paragraph (1)(B) with amounts from the grant and returned from the training as employees of the recipient; and\n**(B)**\nthe number of law enforcement officers or recruits described in subparagraph (A) who remain an employee of the recipient.",
      "versionDate": "2025-05-20",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-15",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strong Communities Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T15:53:20Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-03T15:52:57Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-03T15:53:04Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-03T15:53:10Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-03T15:53:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-05T13:11:06Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1316is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1316rs.xml"
        }
      ],
      "type": "Reported in Senate"
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
      "updateDate": "2025-10-23T11:18:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strong Communities Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strong Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide that COPS grant funds may be used for local law enforcement recruits to attend schools or academies if the recruits agree to serve in precincts of law enforcement agencies in their communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:18:28Z"
    }
  ]
}
```
