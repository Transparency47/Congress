# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6998?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6998
- Title: Renewed Hope Act
- Congress: 119
- Bill type: HR
- Bill number: 6998
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-05-18T15:26:43Z
- Update date including text: 2026-05-18T15:26:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-13 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-01-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-13 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6998",
    "number": "6998",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Renewed Hope Act",
    "type": "HR",
    "updateDate": "2026-05-18T15:26:43Z",
    "updateDateIncludingText": "2026-05-18T15:26:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
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
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
            "date": "2026-01-13T14:39:55Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-09T14:01:40Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "OH"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "MP"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NE"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "RI"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "CO"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MO"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "FL"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6998ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6998\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Ms. Lee of Florida (for herself and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo enhance hiring authorities at the Department of Homeland Security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Renewed Hope Act .\n#### 2. Image audio forensics hiring and training programs at the Department of Homeland Security\n##### (a) Additional personnel\nThe Secretary of Homeland Security shall hire, train, and assign not fewer than\u2014\n**(1)**\n40 forensics analysts to the Victim Identification Laboratory of the Child Exploitation Investigations Unit of Homeland Security Investigations;\n**(2)**\n30 child exploitation investigators to the Victim Identification Laboratory of the Child Exploitation Investigations Unit of Homeland Security Investigations; and\n**(3)**\n130 additional forensics analysts and child exploitation investigators to support identification and rescue of victims of child sexual exploitation and abuse at Homeland Security Investigations offices of the Special Agent in Charge.\n##### (b) Prohibition on reassignment of positions\n**(1) In general**\nA position created under subsection (a) may not be reassigned to another component of the Department of Homeland Security that is outside of the Child Exploitation Investigations Unit of Homeland Security Investigations or the offices of the Special Agent in Charge of Homeland Security Investigations, as applicable.\n**(2) Reassignment of employees**\nAn employee serving in a position created under subsection (a) may be reassigned to another component of the Department of Homeland Security that is outside of the Child Exploitation Investigations Unit of Homeland Security Investigations or the offices of the Special Agent in Charge of Homeland Security Investigations only if the employee elects to be so reassigned.\n##### (c) Employment of experts and consultants\nSection 890A of the Homeland Security Act of 2002 ( 6 U.S.C. 473 ) is amended\u2014\n**(1)**\nby redesignating subsection (g) as subsection (i); and\n**(2)**\nby inserting after subsection (f) the following:\n(g) Employment of Experts and Consultants (1) In general In accordance with section 3109 of title 5, United States Code, at daily rates not to exceed the equivalent rate prescribed for grade GS\u201315 of the General Schedule under section 5332 of such title, the Secretary may procure by contract the temporary (not in excess of 1 year) or intermittent services of experts or consultants to provide image and audio forensic analysis related to victim identification to support efforts to identify, locate, and rescue children seen in videos images and videos of sexual exploitation and abuse. (2) Placement The Secretary shall promulgate guidelines for assigning or detailing participants to positions at the Center, offices of the Special Agent in Charge, offices of the Resident Agent in Charge, and Attach\u00e9 offices. .\n#### 3. Deconfliction of child sexual exploitation and abuse investigations within the department of homeland security\nSection 890A(a) of the Homeland Security Act of 2002 ( 6 U.S.C. 473(a) ) is amended by inserting after paragraph (2) the following:\n(3) Coordination The Secretary shall, with the concurrence of the directors of affected agencies within the Department, establish joint procedures to deconflict, coordinate, and synchronize child sexual exploitation investigations with the Center. (4) NCMEC coordination The Center may establish joint procedures with the National Center for Missing and Exploited Children to deconflict, coordinate, and synchronize child sexual exploitation investigations with the Child Victim Identification Program of the National Center for Missing and Exploited Children. .\n#### 4. Victim identification training program\n##### (a) In general\nThe Secretary of Homeland Security shall establish a Victim Identification Training Program (referred to in this section as the Program ) in the Cyber Crimes Center.\n##### (b) Program\nThe Program shall provide training used to identify victims of sexual exploitation and abuse to\u2014\n**(1)**\nHomeland Security Investigations personnel;\n**(2)**\nFederal, State, local, Tribal, and foreign law enforcement agency personnel engaged in the investigation of crimes of child sexual exploitation and abuse within their respective jurisdictions;\n**(3)**\nCivil service organizations engaged in the prevention of child sexual exploitation and the identification of abuse victims; and\n**(4)**\nThe National Center for Missing and Exploited Children.\n##### (c) Functions\nThe functions of the Program shall include\u2014\n**(1)**\nannual training for participants focused on\u2014\n**(A)**\ntraining on the most current tools and techniques used in victim identification; and\n**(B)**\ntraining on the capabilities of the Victim Identification Laboratory; and\n**(2)**\nincreasing personnel knowledge on how to conduct image, audio, and video enhancements.\n#### 5. Direct hire authority for Homeland Security Investigations\n##### (a) Direct hire\n**(1) In general**\nExcept as provided in paragraph (2), the head of Homeland Security Investigations may appoint, without regard to the provisions of subchapter I of chapter 33 (other than sections 3303 and 3328 of such chapter) of title 5, United States Code, qualified candidates to the positions described in section 2(a).\n**(2) Limitation**\nThe authority under paragraph (1) shall not be available to the head if, during any period, at least 97 percent of such positions are occupied.\n##### (b) Reports\nNot later than 1 year after the date of the enactment of this Act and for each of the 4 following years, the head of Homeland Security Investigations shall submit a report to the Committee on the Judiciary and the Committee on Oversight and Accountability of the House of Representatives, the Committee on the Judiciary and the Committee on Homeland Security and Governmental Affairs of the Senate, and any other relevant congressional committee of jurisdiction. Each such report shall include the following:\n**(1)**\nThe total number of individuals appointed by the head under this section during the preceding year.\n**(2)**\nHow the direct hiring authority under this section is being used by the head.\n#### 6. Application\nThe requirements of each of sections 2 through 4 of this Act, and any amendment made by such sections, shall be carried out not later than the date that is 3 years after the date of the enactment of this Act.\n#### 7. Privacy protections for victims\n##### (a) In general\nA covered person shall\u2014\n**(1)**\nkeep all identifying information and documents concerning a victim of child sexual exploitation or abuse in a secure place to which only individuals working to identify and rescue victims of child sexual exploitation or abuse have access; and\n**(2)**\nnot disclose or use any information or documents concerning a victim of child sexual exploitation or abuse other than for the purposes of\u2014\n**(A)**\ninvestigating or prosecuting individuals for crimes of child sexual exploitation or abuse;\n**(B)**\nconnecting victims\u2014\n**(i)**\nto licensed and trained trauma informed medical professions; or\n**(ii)**\nwith Federal resources available through the Office of Victims of Crime at the Department of Justice;\n**(C)**\ncomplying with any mandatory victim reporting requirements; or\n**(D)**\nsharing information with other law enforcement personnel for the purpose of investigating or prosecuting individuals for crimes of child sexual exploitation or abuse.\n##### (b) Covered person defined\nIn this section, the term covered person means\u2014\n**(1)**\nany Federal, State, or local law enforcement officer; or\n**(2)**\nany other personnel of the Department of Homeland Security,\nworking in, employed by, or detailed to the Child Exploitation Investigations Unit of Homeland Security Investigations or to the offices of the Special Agent in Charge of Homeland Security Investigations.",
      "versionDate": "2026-01-09",
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
            "name": "Congressional oversight",
            "updateDate": "2026-05-18T15:26:38Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-05-18T15:26:27Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2026-05-18T15:26:09Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2026-05-18T15:26:23Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2026-05-18T15:25:40Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2026-05-18T15:26:05Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-05-18T15:25:44Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2026-05-18T15:26:33Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-05-18T15:25:51Z"
          },
          {
            "name": "Missing persons",
            "updateDate": "2026-05-18T15:26:17Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2026-05-18T15:26:42Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2026-05-18T15:26:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-20T14:11:42Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6998ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Renewed Hope Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T04:08:16Z"
    },
    {
      "title": "Renewed Hope Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T04:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance hiring authorities at the Department of Homeland Security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T04:03:15Z"
    }
  ]
}
```
