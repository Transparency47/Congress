# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4688?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4688
- Title: COOL OFF Act
- Congress: 119
- Bill type: HR
- Bill number: 4688
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-30T20:32:54Z
- Update date including text: 2026-03-30T20:32:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4688",
    "number": "4688",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "COOL OFF Act",
    "type": "HR",
    "updateDate": "2026-03-30T20:32:54Z",
    "updateDateIncludingText": "2026-03-30T20:32:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:00:25Z",
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
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TN"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "CO"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "GA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4688ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4688\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Krishnamoorthi (for himself, Mr. Auchincloss , Mr. Casten , Ms. Castor of Florida , Mr. Cohen , Mr. Davis of Illinois , Mr. Carbajal , Mr. Lieu , Mr. Johnson of Georgia , Mr. Khanna , Mr. Keating , Mr. Morelle , Ms. Norton , Mr. Quigley , Ms. Schakowsky , Mr. Thanedar , and Mr. Vargas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for a 3-day waiting period before a person may receive a handgun, with exceptions.\n#### 1. Short title\nThis Act may be cited as the Choosing Our Own Lives Over Fast Firearms Act or the COOL OFF Act .\n#### 2. 3-day waiting period required before receipt of a handgun, with exceptions\n##### (a) Transfers between persons who are not firearms licensees\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) (1) Except as provided in paragraph (2), it shall be unlawful for a person not licensed under this chapter, in or affecting interstate or foreign commerce, to receive a handgun from another person not licensed under this chapter unless at least 3 business days (meaning a day on which State offices are open) have elapsed since the recipient most recently offered to take possession of the handgun. (2) Paragraph (1) shall not apply with respect to a handgun transfer that meets the conditions of subsection (t)(7). .\n##### (b) Transfers by firearms licensees to non-Licensees\nSection 922(t) of such title is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking and at the end of subparagraph (C)(iii)(II);\n**(B)**\nby striking the period and inserting ; and at the end of subparagraph (D); and\n**(C)**\nby adding at the end the following:\n(E) in the case of a handgun transfer that does not meet the conditions of paragraph (7), 3 business days (meaning a day on which State offices are open) have elapsed since the licensee contacted the system. ; and\n**(2)**\nby adding at the end the following:\n(7) A handgun transfer meets the conditions of this paragraph if\u2014 (A) the transferee is a law enforcement agency or any law enforcement officer, armed private security professional, or member of the armed forces, to the extent the officer, professional, or member is acting within the course and scope of employment and official duties; (B) the transfer is a loan between spouses, between domestic partners, between parents and their children, between siblings, between aunts or uncles and their nieces or nephews, or between grandparents and their grandchildren, for a lawful purpose; (C) the transfer is temporary and necessary to prevent imminent death or great bodily harm, if the possession by the transferee lasts only as long as immediately necessary to prevent the imminent death or great bodily harm; or (D) the transfer is temporary and the transferor has no reason to believe that the transferee will use or intends to use the firearm in a crime or is prohibited from possessing firearms under State or Federal law, and the transfer takes place and the transferee\u2019s possession of the firearm is exclusively\u2014 (i) at a shooting range or in a shooting gallery or other area designated for the purpose of target shooting; (ii) while reasonably necessary for the purposes of hunting, trapping, or fishing, if the transferor\u2014 (I) has no reason to believe that the transferee intends to use the firearm in a place where it is illegal; and (II) has reason to believe that the transferee will comply with all licensing and permit requirements for such hunting, trapping, or fishing; or (iii) while in the presence of the transferor. .\n##### (c) Penalties\nSection 924(a)(1)(B) of such title is amended by striking or (q) and inserting (q), or (aa) .\n##### (d) Effective date\nThe amendments made by this section shall apply to conduct engaged in after the 90-day period that begins with the date of the enactment of this Act.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-17T17:16:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4688",
          "measure-number": "4688",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4688v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Choosing Our Own Lives Over Fast Firearms Act or the COOL OFF Act</b></p> <p>This bill establishes a three-day waiting period for certain handgun transfers.</p> <p>Specifically, the bill makes it unlawful for a licensed importer, manufacturer, or dealer to sell or transfer a handgun to an unlicensed individual unless three business days have elapsed since the licensee initiated a background check. A violator is subject to criminal penalties\u2014a fine, up to one year in prison, or both.</p> <p>Additionally, the bill makes it unlawful for an unlicensed individual to receive a handgun from another unlicensed individual unless at least three business days have elapsed since the recipient most recently offered to take possession of the handgun. A violator is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p> <p>The three-day waiting period does not apply to certain handgun transfers, such as for a loan between spouses for a lawful purpose. </p>"
        },
        "title": "COOL OFF Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4688.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Choosing Our Own Lives Over Fast Firearms Act or the COOL OFF Act</b></p> <p>This bill establishes a three-day waiting period for certain handgun transfers.</p> <p>Specifically, the bill makes it unlawful for a licensed importer, manufacturer, or dealer to sell or transfer a handgun to an unlicensed individual unless three business days have elapsed since the licensee initiated a background check. A violator is subject to criminal penalties\u2014a fine, up to one year in prison, or both.</p> <p>Additionally, the bill makes it unlawful for an unlicensed individual to receive a handgun from another unlicensed individual unless at least three business days have elapsed since the recipient most recently offered to take possession of the handgun. A violator is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p> <p>The three-day waiting period does not apply to certain handgun transfers, such as for a loan between spouses for a lawful purpose. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr4688"
    },
    "title": "COOL OFF Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Choosing Our Own Lives Over Fast Firearms Act or the COOL OFF Act</b></p> <p>This bill establishes a three-day waiting period for certain handgun transfers.</p> <p>Specifically, the bill makes it unlawful for a licensed importer, manufacturer, or dealer to sell or transfer a handgun to an unlicensed individual unless three business days have elapsed since the licensee initiated a background check. A violator is subject to criminal penalties\u2014a fine, up to one year in prison, or both.</p> <p>Additionally, the bill makes it unlawful for an unlicensed individual to receive a handgun from another unlicensed individual unless at least three business days have elapsed since the recipient most recently offered to take possession of the handgun. A violator is subject to criminal penalties\u2014a fine, up to five years in prison, or both.</p> <p>The three-day waiting period does not apply to certain handgun transfers, such as for a loan between spouses for a lawful purpose. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr4688"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4688ih.xml"
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
      "title": "COOL OFF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COOL OFF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Choosing Our Own Lives Over Fast Firearms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a 3-day waiting period before a person may receive a handgun, with exceptions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:32Z"
    }
  ]
}
```
