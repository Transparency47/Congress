# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4173
- Title: Preventing Pretrial Gun Purchases Act
- Congress: 119
- Bill type: HR
- Bill number: 4173
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-01-10T07:11:45Z
- Update date including text: 2026-01-10T07:11:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4173",
    "number": "4173",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Preventing Pretrial Gun Purchases Act",
    "type": "HR",
    "updateDate": "2026-01-10T07:11:45Z",
    "updateDateIncludingText": "2026-01-10T07:11:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:02:00Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "RI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "GA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "DC"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "HI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "MA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4173ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4173\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Goldman of New York (for himself, Ms. Schakowsky , Mr. Magaziner , Mr. Frost , Mr. Johnson of Georgia , Mr. Garcia of California , Ms. Norton , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo ensure that the background check system used for firearms purchases denies a firearm to a person prohibited from possessing a firearm by a lawful court order governing the pretrial release of the person.\n#### 1. Short title\nThis Act may be cited as the Preventing Pretrial Gun Purchases Act .\n#### 2. Amendments to the Gun Control Act of 1968\n##### (a) Section 921\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) The term pretrial release order means an order of a Federal, State, Tribal, or local court that governs the release of an arrested person pending the trial of the person for a crime. .\n##### (b) Section 922\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (10), by striking or at the end;\n**(B)**\nin paragraph (11), by striking the period and inserting ; or ; and\n**(C)**\nby inserting after paragraph (11) the following:\n(12) is subject to a pretrial release order that prohibits the person from purchasing, possessing, or receiving firearms. ; and\n**(2)**\nin subsection (t)\u2014\n**(A)**\nin paragraph (1)(B)(ii), by striking receipt of a firearm and all that follows through section and inserting knowing sale or disposition of a firearm by the licensee to such other person or the receipt of a firearm by such other person would violate subsection (d), (g), or (n) of this section ;\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by striking receipt and all that follows through (n) and inserting the knowing sale or disposition of a firearm to the person or the receipt of a firearm by the person would not violate subsection (d), (g), or (n) ;\n**(C)**\nin paragraph (3)(A)(ii), by striking that possession and inserting that knowing sale or disposition of a firearm by a licensee to such other person or possession ;\n**(D)**\nin paragraph (4)\u2014\n**(i)**\nby striking receipt and all that follows through (n) and inserting knowing sale or disposition of a firearm by a licensee to such other person or the receipt of a firearm by such other person would violate subsection (d), (g), or (n) ; and\n**(ii)**\nby inserting a comma after State ; and\n**(E)**\nin paragraph (5)\u2014\n**(i)**\nby striking receipt and all that follows through (n) and inserting knowing sale or disposition of a firearm by a licensee to such other person or receipt of a firearm by such other person would violate subsection (d), (g), or (n) ; and\n**(ii)**\nby inserting a comma after State .\n#### 3. Conforming amendments\n##### (a) Section 923\nSection 923(d)(1)(B) of title 18, United States Code, is amended by striking under section 922(g) and (n) of this chapter and inserting by subsection (g) or (n) of section 922 and is not a person to whom the knowing sale or disposition of any firearm or ammunition is prohibited by section 922(d) .\n##### (b) Section 925 A\nSection 925A(2) of title 18, United States Code, is amended by inserting and to whom the knowing sale or disposition of a firearm was not prohibited by subsection (d) of that section or State law before the comma.\n##### (c) Brady Handgun Violence Prevention Act\nSection 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) is amended\u2014\n**(1)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (A), by striking for whom receipt and all that follows through (g) and inserting to whom the knowing sale or disposition of or for whom receipt of a firearm would violate subsection (d), (g), ;\n**(B)**\nin subparagraph (C), by striking (g) and inserting (d), (g), ;\n**(C)**\nin subparagraph (F)(iii)(I), by striking (g) or (n) and inserting (d), (g), or (n) ; and\n**(D)**\nin subparagraph (G)(i), by striking (g) or (n) and inserting (d), (g), or (n) ;\n**(2)**\nin subsection (g), by striking receipt of a firearm by a prospective transferee would violate subsection (g) or (n) and inserting the knowing sale or disposition of a firearm to or receipt of a firearm by a prospective transferee would violate subsection (d), (g), or (n) ; and\n**(3)**\nin subsection (i)(2), by striking all that follows after respect to persons and inserting to whom the knowing sale or disposition of, or for whom receipt of, a firearm is prohibited by subsection (d), (g), or (n) of section 922 of title 18, United States Code, or State law. .\n##### (d) NICS Improvement Amendments Act of 2007\nTitle I of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40911 et seq. ) is amended\u2014\n**(1)**\nin section 101(b) ( 34 U.S.C. 40911(b) )\u2014\n**(A)**\nin paragraph (1)(A), by striking a person is disqualified from possessing or receiving a firearm under subsection (g) and inserting the knowing sale or disposition of a firearm to a person or receipt of a firearm by a person is prohibited by subsection (d), (g), ; and\n**(B)**\nin paragraph (2)(A)\u2014\n**(i)**\nby striking after the and inserting after a court martial imposes a pretrial release order or the ; and\n**(ii)**\nby striking a member of the Armed Forces involved in such proceeding is disqualified from possessing or receiving a firearm under subsection (g) or (n) and inserting the knowing sale or disposition of a firearm to or receipt of a firearm by a member of the Armed Forces is prohibited by subsection (d), (g), or (n) ; and\n**(2)**\nin section 102 ( 34 U.S.C. 40912 )\u2014\n**(A)**\nin subsection (b)(3), by striking are prohibited from possessing or receiving a firearm under subsection (g) and inserting are described in one of the categories under subsection (d), (g), ; and\n**(B)**\nin subsection (c)(1)(A), by inserting the knowing sale or disposition of a firearm to a person would be prohibited under subsection (d) of section 922 of title 18, United States Code, or applicable State law or whether after determination of whether .\n#### 4. Funds for States that report pretrial orders restricting firearm possession to NICS\n##### (a) Definition\nIn this section, the term covered pretrial release order means an order of a State, Tribal, or local court that governs the release of an arrested individual pending the trial of the individual for a crime, and which prohibits the individual from possessing a firearm or ammunition (as such terms are defined in section 921 of title 18, United States Code).\n##### (b) Authorization\nThe Attorney General may make grants to States and Indian Tribes for the purpose of reporting information about covered pretrial release orders to the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ).\n##### (c) Applications\nThe chief executive of a State or Indian Tribe seeking a grant under this section shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require.\n##### (d) Clarification\nGrants made under this section shall be in addition to any amount that a State or Indian Tribe receives under section 302(c)(19) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10132(c)(19) ) (commonly referred to as the National Criminal History Improvement Program ) or section 103 of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40913 ) (commonly referred to as the NICS Act Record Improvement Program ).\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated $25,000,000 for each of fiscal years 2026 through 2030 to carry out this section.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-06-26",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2186",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventing Pretrial Gun Purchases Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-16T13:16:06Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4173ih.xml"
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
      "title": "Preventing Pretrial Gun Purchases Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing Pretrial Gun Purchases Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that the background check system used for firearms purchases denies a firearm to a person prohibited from possessing a firearm by a lawful court order governing the pretrial release of the person.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:32Z"
    }
  ]
}
```
