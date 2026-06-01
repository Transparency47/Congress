# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5453
- Title: RRLEF Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5453
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-05-13T08:06:26Z
- Update date including text: 2026-05-13T08:06:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5453",
    "number": "5453",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "A000380",
        "district": "1",
        "firstName": "Gabe",
        "fullName": "Rep. Amo, Gabe [D-RI-1]",
        "lastName": "Amo",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "RRLEF Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:26Z",
    "updateDateIncludingText": "2026-05-13T08:06:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:06:40Z",
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
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MD"
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
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "RI"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MA"
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
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-18",
      "state": "DC"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NC"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "PA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "NV"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "GA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "GA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5453ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5453\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Amo (for himself, Mr. Raskin , Mr. Johnson of Georgia , Mr. Magaziner , Ms. Bonamici , Mr. Jackson of Illinois , Mr. Moulton , Mr. Goldman of New York , Mr. Mullin , Ms. Jayapal , Ms. Kelly of Illinois , Ms. Norton , Mr. Espaillat , Mr. Swalwell , Mr. Smith of Washington , Ms. Dean of Pennsylvania , Mr. Frost , and Mr. Casten ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility under the Edward Byrne Memorial Justice Assistance Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible Retirement of Law Enforcement Firearms Act of 2025 or the RRLEF Act of 2025 .\n#### 2. Eligibility under Edward Byrne Memorial Justice Assistance Grant Program\n##### (a) Certification requirement\nSection 502 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10153 ) is amended\u2014\n**(1)**\nin subsection (a)(5)\u2014\n**(A)**\nin subparagraph (C), by striking and ;\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) the applicant, and each grantee or subgrantee under the jurisdiction of the applicant, shall not transfer a firearm to, or purchase a firearm from, a licensed dealer that is on the list of covered licensed dealers most recently published at the time of certification by the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives under section 2(b)(2) of the RRLEF Act of 2025. ; and\n**(2)**\nby adding at the end the following:\n(c) Definitions In this section\u2014 (1) the term covered licensed dealer means a licensed dealer with respect to whom, in not less than two of the three calendar years prior to the publication of the list under section 2(b)(2) of the RRLEF Act of 2025, the National Tracing Center of the Bureau of Alcohol, Tobacco, Firearms and Explosives has traced to the firearms business of such licensed dealer, in such calendar years, not less than 25 firearms that had a short time-to-crime; (2) the terms licensed dealer and firearm have the meaning given such terms, respectively, in section 921(a) of title 18, United States Code; and (3) the term short time-to-crime means, a period of not more than three calendar years between the date of the last known retail sale of a firearm and the date a law enforcement agency recovers such firearm as a result of such firearm being purchased for, possessed during, or used in, an actual or suspected criminal offense. .\n##### (b) Public disclosure of database information of Bureau of Alcohol, Tobacco, Firearms and Explosives\nNot later than 120 days after the date of the enactment of this Act, and annually thereafter, the Attorney General, acting through the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives shall\u2014\n**(1)**\nnotify a State or local law enforcement agency if any firearm (as such term is defined in section 921(a) of title 18, United States Code) that was transferred by such agency was used, or suspected of being used, in the commission of a criminal offense, as traced by the National Tracing Center of the Bureau; and\n**(2)**\nmake publicly available on the internet website of the Bureau a list of each covered licensed dealer (as such term is defined in section 502(c) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10153(c) )).\n##### (c) Repeal of certain limitations on public disclosure of database information of Bureau of Alcohol, Tobacco, Firearms and Explosives\n**(1) Public Law 112\u201355**\nThe 6th proviso under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses\u201d in title II of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 18 U.S.C. 923 note; Public Law 112\u201355 ; 125 Stat. 609\u2013610) is amended by striking and in each fiscal year thereafter .\n**(2) Public Law 111\u2013117**\nThe 6th proviso under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses\u201d in title II of division B of the Consolidated Appropriations Act, 2010 ( 18 U.S.C. 923 note; Public Law 111\u2013117 ; 123 Stat. 3128\u20133129) is amended by striking beginning in fiscal year 2010 and thereafter and inserting in fiscal year 2010 .\n**(3) Public Law 111\u20138**\nThe 6th proviso under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses\u201d in title II of division B of the Omnibus Appropriations Act, 2009 ( 18 U.S.C. 923 note; Public Law 111\u20138 ; 123 Stat. 574\u2013576) is amended by striking beginning in fiscal year 2009 and thereafter and inserting in fiscal year 2009 .\n**(4) Public Law 110\u2013161**\nThe 6th proviso under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses\u201d in title II of division B of the Consolidated Appropriations Act, 2008 ( 18 U.S.C. 923 note; Public Law 110\u2013161 ; 121 Stat. 1903\u20131904) is amended by striking beginning in fiscal year 2008 and thereafter and inserting in fiscal year 2008 .\n**(5) Public Law 109\u2013108**\nThe 6th proviso under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u2014Salaries and Expenses\u201d in title I of the Science, State, Justice, Commerce, and Related Agencies Appropriations Act, 2006 ( 18 U.S.C. 923 note; Public Law 109\u2013108 ; 119 Stat. 2295\u20132296) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2006 .\n**(6) Public Law 108\u2013447**\nThe 6th proviso under the heading \u201cSalaries and Expenses\u201d under the heading \u201cBureau of Alcohol, Tobacco, Firearms and Explosives\u201d in title I of division B of the Consolidated Appropriations Act, 2005 ( 18 U.S.C. 923 note; Public Law 108\u2013447 ; 118 Stat. 2859) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2005 .\n**(7) Public Law 108\u20137**\nSection 644 under the heading General Provisions in title VI of division J of the Treasury and General Government Appropriations Act of 2003 ( 5 U.S.C. 552 note; Public Law 108\u20137 ; 117 Stat. 473) is amended by striking with respect to any fiscal year and inserting with respect to fiscal year 2003 .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2863",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "RRLEF Act of 2025",
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
        "updateDate": "2025-11-18T16:34:04Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5453ih.xml"
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
      "title": "RRLEF Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RRLEF Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Responsible Retirement of Law Enforcement Firearms Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 with respect to eligibility under the Edward Byrne Memorial Justice Assistance Grant Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:23Z"
    }
  ]
}
```
