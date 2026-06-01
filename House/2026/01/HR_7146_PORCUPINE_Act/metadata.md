# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7146?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7146
- Title: PORCUPINE Act
- Congress: 119
- Bill type: HR
- Bill number: 7146
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-05-13T08:06:17Z
- Update date including text: 2026-05-13T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7146",
    "number": "7146",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "PORCUPINE Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:17Z",
    "updateDateIncludingText": "2026-05-13T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "KS"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "GU"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "AL"
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
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "MT"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "FL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "VA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "IA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "KY"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TN"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MD"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DE"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "SC"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "HI"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7146ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7146\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Wittman (for himself, Mr. Bera , Mr. Davis of North Carolina , and Mr. Mackenzie ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act or the PORCUPINE Act .\n#### 2. Modification of certification and reporting requirements under the Arms Export Control Act\n##### (a) In general\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 22 U.S.C. 2753 )\u2014\n**(A)**\nin subsection (b)(2), by inserting Taiwan, before or the ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (2)(B), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (3)(A)(i), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(2)**\nin section 21 ( 22 U.S.C. 2761 )\u2014\n**(A)**\nin subsection (e)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1)(A), by striking or Israel and inserting Israel, or Taiwan ; and\n**(ii)**\nin paragraph (2), by striking or Israel and inserting Israel, or Taiwan ;\n**(3)**\nin section 36 ( 22 U.S.C. 2776 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), in the undesignated matter following subparagraph (P), in the second sentence, by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (2), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(ii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(C)**\nin subsection (d)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(4)**\nin section 62(c)(1) ( 22 U.S.C. 2796a(c)(1) ), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(5)**\nin section 63(a)(2) ( 22 U.S.C. 2796b(a)(2) ), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan .\n##### (b) Report\nNot later than two years after the date of the enactment of this section, and every two years thereafter, the Secretary of State shall submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report on the implementation and effectiveness of the amendments made by this section.\n#### 3. Feasibility assessment of expedited licensing for allies transferring military equipment to Taiwan\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall conduct an assessment of the feasibility of establishing an expedited decision-making process for third-party transfers of defense articles and services from North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, New Zealand, or Israel to Taiwan, including transfers and re-transfers of United States-origin grant, Foreign Military Sales, and Direct Commercial Sales end-items not covered by an exemption under the International Traffic in Arms Regulations under subchapter M of chapter I of title 22, Code of Federal Regulations.\n##### (b) Elements\nThe assessment required by subsection (a) shall include an assessment of the following:\n**(1)**\nThe availability of such an expedited decision-making process for classified and unclassified items.\n**(2)**\nThe feasibility of requiring\u2014\n**(A)**\nthe approval, return, or denial of any licensing application to export defense articles and services that is related to a government-to-government agreement within 15 days after the submission of such application; and\n**(B)**\nthe completion of the review of all other licensing requests not later than 30 days after the submission of such application.\n##### (c) Briefing\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall provide the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives with a briefing on the outcome of the assessment required by subsection (a).\n#### 4. Rule of construction\nNothing in this Act may be construed to alter the policy of the United States toward Taiwan as specified in the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ).\n#### 5. Sunset\nThis Act shall cease to have effect on the date that is 7 years after the date of the enactment of this Act.",
      "versionDate": "2026-01-16",
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
        "actionDate": "2025-12-15",
        "actionTime": "16:19:16",
        "text": "Held at the desk."
      },
      "number": "1744",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PORCUPINE Act",
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
        "name": "International Affairs",
        "updateDate": "2026-02-11T14:26:50Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7146ih.xml"
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
      "title": "PORCUPINE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T10:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PORCUPINE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T10:18:24Z"
    }
  ]
}
```
