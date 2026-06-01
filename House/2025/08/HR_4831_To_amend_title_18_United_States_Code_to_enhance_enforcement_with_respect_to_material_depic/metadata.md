# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4831?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4831
- Title: ENFORCE Act
- Congress: 119
- Bill type: HR
- Bill number: 4831
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-05-08T08:06:51Z
- Update date including text: 2026-05-08T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4831",
    "number": "4831",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000812",
        "district": "2",
        "firstName": "Ann",
        "fullName": "Rep. Wagner, Ann [R-MO-2]",
        "lastName": "Wagner",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "ENFORCE Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:51Z",
    "updateDateIncludingText": "2026-05-08T08:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:02:40Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NJ"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "TN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "KS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "AR"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IN"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NE"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "NC"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4831ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4831\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mrs. Wagner (for herself, Mr. Van Drew , and Mr. Cohen ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to enhance enforcement with respect to material depicting obscene child sexual abuse or constituting child pornography, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Necessary Federal Offenses Regarding Child Exploitation Act or the ENFORCE Act .\n#### 2. Clarifying production with respect to material constituting or containing child pornography\nSection 2252A of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking paragraph (7) and inserting the following:\n(7) knowingly produces child pornography, as defined in section 2256(8)(C), that\u2014 (A) the person knows, or has reason to know, will be mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce; (B) was produced using materials that have been mailed, shipped, or transported in or affecting interstate or foreign commerce; or (C) has been mailed, shipped, or transported using any means or facility of interstate or foreign commerce or in or affecting interstate or foreign commerce, ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking or (6) and inserting (6), or (7) ; and\n**(B)**\nby striking paragraph (3).\n#### 3. Enhancing enforcement with respect to obscene visual representations of child sexual abuse\n##### (a) Removing the statute of limitations for obscene visual representations of child sexual abuse\nSection 3299 of title 18, United States Code, is amended by inserting 1466A or before 1591 .\n##### (b) Including crimes of obscene visual representations of child sexual abuse in sex offender registration\nSection 111(5)(A)(iii) of the Adam Walsh Child Protection and Safety Act of 2006 ( 34 U.S.C. 20911(5)(A)(iii) ) is amended by inserting 1466A or before 1591 .\n##### (c) Prohibition on reproduction of obscene visual representations of child sexual abuse in discovery\nSection 1466A of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating subsection (f) as subsection (g); and\n**(2)**\nby inserting after subsection (e) the following:\n(f) Prohibition on reproduction of obscene visual depictions of child sexual abuse In any criminal proceeding brought under this section\u2014 (1) any visual depiction involved in a violation of this section shall remain in the care, custody, and control of either the Government or the court in the same manner specified for child pornography in paragraphs (1) and (2) of section 3509(m); and (2) any identifiable minor, as that term is defined in section 2256(9), depicted in any visual depiction involved in a violation of this section may have access to such depiction in the same manner specified for a victim, with respect to child pornography depicting the victim, in section 3509(m)(3). .\n##### (d) Presumption of detention for violations of section 1466A pending trial\nSection 3142 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(1)(B), in the undesignated matter following clause (xiv), by striking that involves and all that follows through 2425 of this title and inserting that involves an offense described in subsection (e)(3)(E) ; and\n**(2)**\nin subsection (e)(3), by striking subparagraph (E) and inserting the following:\n(E) an offense\u2014 (i) involving a minor victim under section 1201, 1591, 2241(a), 2241(b), 2242, 2244(a)(1), 2245, 2421, or 2422(a) of this title; or (ii) under section 1466A(a), 2241(c), 2251A, 2252(a)(1), 2252(a)(2), 2252(a)(3), 2252A(a)(1), 2252A(a)(2), 2252A(a)(3), 2252A(a)(4), 2260, 2422(b), 2423, or 2425 of this title. .\n##### (e) Supervised release for violations of section 1466A after imprisonment\nSection 3583(k) of title 18, United States Code, is amended, in the first sentence, by inserting 1466A, before 1591, .",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-12-17",
        "actionTime": "10:22:12",
        "text": "Held at the desk."
      },
      "number": "3021",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ENFORCE Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-12-17T19:20:51Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-12-17T19:20:51Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-12-17T19:20:51Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-12-17T19:20:51Z"
          },
          {
            "name": "Pornography",
            "updateDate": "2025-12-17T19:20:51Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-12-17T19:20:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-17T16:53:43Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4831ih.xml"
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
      "title": "ENFORCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ENFORCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing Necessary Federal Offenses Regarding Child Exploitation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to enhance enforcement with respect to material depicting obscene child sexual abuse or constituting child pornography, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:19Z"
    }
  ]
}
```
