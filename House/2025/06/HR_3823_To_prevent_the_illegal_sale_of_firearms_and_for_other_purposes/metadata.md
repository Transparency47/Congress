# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3823
- Title: TRACE Act
- Congress: 119
- Bill type: HR
- Bill number: 3823
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-06-30T13:10:40Z
- Update date including text: 2025-06-30T13:10:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3823",
    "number": "3823",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "Q000023",
        "district": "5",
        "firstName": "Mike",
        "fullName": "Rep. Quigley, Mike [D-IL-5]",
        "lastName": "Quigley",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "TRACE Act",
    "type": "HR",
    "updateDate": "2025-06-30T13:10:40Z",
    "updateDateIncludingText": "2025-06-30T13:10:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:01:35Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "GA"
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
      "sponsorshipDate": "2025-06-06",
      "state": "DC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "FL"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MO"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MO"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CO"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "WA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "TX"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NC"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "VA"
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
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3823ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3823\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Quigley (for himself, Mr. Johnson of Georgia , Ms. Norton , Mr. Thanedar , Mr. Moulton , Mr. Torres of New York , Mr. Kennedy of New York , Mrs. Cherfilus-McCormick , Mr. Davis of Illinois , Mr. Krishnamoorthi , Mr. Cleaver , Mr. Auchincloss , Mr. Bell , Mr. Neguse , Mr. Latimer , Mr. DeSaulnier , Mr. Casten , Mr. Smith of Washington , Ms. Johnson of Texas , Mrs. Foushee , Mr. Beyer , Ms. Schakowsky , and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prevent the illegal sale of firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Trafficking Reduction And Criminal Enforcement Act or the TRACE Act .\n#### 2. Regulatory requirement to mark firearms with second, hidden serial number\n##### (a) In general\nWithin 12 months after the date of the enactment of this Act, the Attorney General shall promulgate final regulations that require each firearm manufactured in the United States on or after the effective date of the regulation, to be marked with a serial number that is located inside the receiver of the firearm or that is visible only in infrared light, in addition to the serial number with which the firearm is otherwise required by law to be marked.\n##### (b) Definition of receiver\nSection 921(a) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby inserting , including an unfinished frame or receiver after such weapon ; and\n**(B)**\nby striking or (D) any destructive device and inserting ; (D) any destructive device; or (E) any combination of parts designed or intended for use in converting any device into a firearm and from which a firearm may be readily assembled ;\n**(2)**\nin paragraph (10)\u2014\n**(A)**\nby striking and the and inserting the ; and\n**(B)**\nby inserting ; and the term manufacturing firearms shall include assembling a functional firearm from an unfinished frame or receiver or from molding, machining, or 3D printing a frame or receiver, and shall not include making or fitting special barrels, stocks, or trigger mechanisms to firearms before the period; and\n**(3)**\nby inserting after paragraph (30) the following:\n(31) The term unfinished frame or receiver means any forging, casting, printing, extrusion, machined body or similar article that\u2014 (A) has reached a stage in manufacture at which it may readily be completed, assembled, or converted to be used as the frame or receiver of a functional firearm; or (B) is marketed or sold to the public to become or be used as the frame or receiver of a functional firearm once completed, assembled, or converted. .\n#### 3. Requirement to preserve instant criminal background check records for 180 days\n##### (a) In general\nSection 922(t)(2)(C) of title 18, United States Code, is amended by inserting after the 180-day period that begins with the date the system complies with subparagraphs (A) and (B), before destroy .\n##### (b) Conforming amendment\nSection 511 of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 34 U.S.C. 40901 note; Public Law 112\u201355 ; 125 Stat. 632) is amended\u2014\n**(1)**\nby striking for\u2014 and all that follows through (1) ; and\n**(2)**\nby striking the semicolon and all that follows and inserting a period.\n##### (c) Regulations\nWithin 180 days after the date of the enactment of this Act, the Attorney General shall prescribe regulations to implement the amendments made by this section.\n#### 4. Requirement that licensed firearms dealers conduct physical check of their firearms business inventory\n##### (a) In general\nSection 923(g) of title 18, United States Code, is amended by adding at the end the following:\n(8) Each licensee shall conduct a physical check of the firearms inventory of the business of the licensee licensed under this chapter, in accordance with regulations which shall be prescribed by the Attorney General. .\n##### (b) Conforming amendment\nThe matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses in title II of division B of the Consolidated and Further Continuing Appropriations Act, 2013 ( 18 U.S.C. 923 note; Public Law 113\u20136 ; 127 Stat. 247\u2013248) is amended by striking the 5th proviso.\n##### (c) Regulations\nWithin 180 days after the date of the enactment of this Act, the Attorney General shall prescribe regulations to implement section 923(g)(8) of title 18, United States Code.\n#### 5. Elimination of certain limitations\n##### (a) Consolidated and Further Continuing Appropriations Act, 2012\nTitle II of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 18 U.S.C. 923 note; Public Law 112\u201355 ; 125 Stat. 609\u2013610) is amended in the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 1st, 6th, and 7th provisos.\n##### (b) Consolidated Appropriations Act, 2010\nDivision B of the Consolidated Appropriations Act, 2010 ( Public Law 111\u2013117 ) is amended\u2014\n**(1)**\nin title II\u2014\n**(A)**\nin the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking beginning in fiscal year 2010 and thereafter and inserting in fiscal year 2010 ; and\n**(B)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 511, to read as follows:\n511. None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (c) Omnibus Appropriations Act, 2009\nDivision B of the Omnibus Appropriations Act, 2009 ( Public Law 111\u20138 ) is amended\u2014\n**(1)**\nin title II\u2014\n**(A)**\nin the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking beginning in fiscal year 2009 and thereafter and inserting in fiscal year 2009 ; and\n**(B)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 511, to read as follows:\n511. None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (d) Consolidated Appropriations Act, 2008\nDivision B of the Consolidated Appropriations Act, 2008 ( Public Law 110\u2013161 ) is amended\u2014\n**(1)**\nin title II\u2014\n**(A)**\nin the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking beginning in fiscal year 2008 and thereafter and inserting in fiscal year 2008 ; and\n**(B)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 512, to read as follows:\n512. None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (e) Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2006\nThe Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2006 ( Public Law 109\u2013108 ) is amended\u2014\n**(1)**\nin title I\u2014\n**(A)**\nin the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking with respect to any fiscal year ; and\n**(B)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 611, to read as follows:\n611. None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (f) Consolidated Appropriations Act, 2005\nDivision B of the Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2005 ( Public Law 108\u2013447 ) is amended\u2014\n**(1)**\nin title I\u2014\n**(A)**\nin the 6th proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking with respect to any fiscal year ; and\n**(B)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 615, to read as follows:\n615. None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (g) Consolidated Appropriations Act, 2004\nDivision B of the Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2004 ( Public Law 108\u2013199 ) is amended\u2014\n**(1)**\nin the matter under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives \u2014 Salaries and Expenses by striking the 7th proviso; and\n**(2)**\nin section 617(a), to read as follows:\n(a) None of the funds appropriated pursuant to this Act or any other provision of law may be used for the implementation of any tax or fee in connection with the implementation of subsection 922(t) of title 18, United States Code. .\n##### (h) Consolidated Appropriations Resolution, 2003\nDivision J of the Consolidated Appropriations Resolution, 2003 ( 5 U.S.C. 552 note; Public Law 108\u20137 ; 117 Stat. 473\u2013474) is amended in section 644 by striking or any other Act with respect to any fiscal year .",
      "versionDate": "2025-06-06",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-30T13:10:40Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3823ih.xml"
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
      "title": "TRACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trafficking Reduction And Criminal Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent the illegal sale of firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:12Z"
    }
  ]
}
```
