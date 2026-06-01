# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7564
- Title: Jaime’s Law
- Congress: 119
- Bill type: HR
- Bill number: 7564
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-04-30T08:06:40Z
- Update date including text: 2026-04-30T08:06:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7564",
    "number": "7564",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000797",
        "district": "25",
        "firstName": "Debbie",
        "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
        "lastName": "Wasserman Schultz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Jaime\u2019s Law",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:40Z",
    "updateDateIncludingText": "2026-04-30T08:06:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:05:05Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CO"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "GA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-20",
      "state": "MA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7564ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7564\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Ms. Wasserman Schultz introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prevent the purchase of ammunition by prohibited purchasers.\n#### 1. Short title\nThis Act may be cited as Jaime\u2019s Law .\n#### 2. Purpose\nThe purpose of this Act is to enhance the background check process in the United States to prevent the purchase of ammunition by individuals who are prohibited from doing so under Federal and State law.\n#### 3. Transfers of firearms or ammunition\n##### (a) In general\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking subsection (s);\n**(2)**\nby redesignating subsection (t) as subsection (s);\n**(3)**\nin subsection (s), as so redesignated\u2014\n**(A)**\nby inserting or ammunition after firearm each place it appears except in subparagraphs (B)(ii) and (C) of paragraph (1);\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B)(ii), by inserting in the case of a firearm, before 3 ; and\n**(ii)**\nin subparagraph (C), in the matter preceding clause (i), by inserting the transfer of a firearm to before a person less ; and\n**(C)**\nin paragraph (3)(C)(ii), by striking the chief law enforcement officer (as defined in subsection (s)(8)) and inserting the relevant chief of police, sheriff, or other equivalent official, or the designee of any such individual ; and\n**(4)**\nby inserting after subsection (s), as so redesignated, the following:\n(t) (1) (A) It shall be unlawful for any person who is not a licensed importer, licensed manufacturer, or licensed dealer to transfer ammunition to any other person who is not so licensed, unless a licensed importer, licensed manufacturer, or licensed dealer has first taken possession of the ammunition for the purpose of complying with subsection (s). (B) Upon taking possession of ammunition under subparagraph (A), a licensee shall comply with all requirements of this chapter as if the licensee were transferring ammunition from the inventory of the licensee to the unlicensed transferee. (C) If a transfer of ammunition described in subparagraph (A) will not be completed for any reason after a licensee takes possession of the ammunition (including because the transfer of the ammunition to, or receipt of the ammunition by, the transferee would violate this chapter), the return of the ammunition to the transferor by the licensee shall not constitute the transfer of ammunition for purposes of this chapter. (2) Paragraph (1) shall not apply to\u2014 (A) a law enforcement agency or any law enforcement officer, armed private security professional, or member of the Armed Forces, to the extent the officer, professional, or member is acting within the course and scope of employment and official duties; (B) a transfer that is a loan or bona fide gift between spouses, between domestic partners, between parents and their children, including step-parents and their step-children, between siblings, between aunts or uncles and their nieces or nephews, or between grandparents and their grandchildren; (C) a transfer to an executor, administrator, trustee, or personal representative of an estate or a trust that occurs by operation of law upon the death of another person; (D) a temporary transfer that is necessary to prevent imminent death or great bodily harm, including harm to self, family, household members, or others, if the possession by the transferee lasts only as long as immediately necessary to prevent the imminent death or great bodily harm, including the harm of domestic violence, dating partner violence, sexual assault, stalking, and domestic abuse; (E) a transfer that is approved by the Attorney General under section 5812 of the Internal Revenue Code of 1986; or (F) a temporary transfer if the transferor has no reason to believe that the transferee will use or intends to use the ammunition in a crime or is prohibited from possessing ammunition under State or Federal law, and the transfer takes place and the transferee's possession of the ammunition is exclusively\u2014 (i) at a shooting range or in a shooting gallery or other area designated for the purpose of target shooting; (ii) while reasonably necessary for the purposes of hunting, trapping, or fishing, if the transferor\u2014 (I) has no reason to believe that the transferee intends to use the ammunition in a place where it is illegal; and (II) has reason to believe that the transferee will comply with all licensing and permit requirements for such hunting, trapping, or fishing; or (iii) while in the presence of the transferor. (3) It shall be unlawful for a licensed importer, licensed manufacturer, or licensed dealer to transfer possession of ammunition to another person who is not so licensed unless the importer, manufacturer, or dealer has provided such other person with a notice of the prohibition under paragraph (1), and such other person has certified that such other person has been provided with this notice on a form prescribed by the Attorney General. .\n##### (b) Technical and conforming amendments\n**(1) United States Code**\nChapter 44 of title 18, United States Code, is amended\u2014\n**(A)**\nin section 922(y)(2), in the matter preceding subparagraph (A), by striking , (g)(5)(B), and (s)(3)(B)(v)(II) and inserting and (g)(5)(B) ;\n**(B)**\nin section 925A, in the matter preceding paragraph (1), by striking subsection (s) or (t) of section 922 and inserting section 922(s) ; and\n**(C)**\nin section 925B\u2014\n**(i)**\nin subsection (a), in the matter preceding paragraph (1), by striking 922(t) and inserting 922(s) ; and\n**(ii)**\nin subsection (b), by striking 922(t) of title 18, United States Code and inserting 922(s) .\n**(2) Brady Handgun Violence Prevention Act**\nSection 103(l) of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901(l) ) is amended, in the matter preceding paragraph (1), by striking (t) and inserting (s) .\n**(3) NICS Improvement Amendments Act of 2007**\nSection 103(f) of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40913(f) ) is amended by striking 922(t) and inserting 922(s) .\n**(4) Consolidated and further continuing appropriations act, 2012**\nSection 511 of title V of division B of the Consolidated and Further Continuing Appropriations Act, 2012 ( 34 U.S.C. 40901 note) is amended by striking subsection 922(t) each place it appears and inserting subsection (s) or (t) of section 922 .\n#### 4. Rules of construction\nNothing in this Act, or any amendment made by this Act, shall be construed to\u2014\n**(1)**\nauthorize the establishment, directly or indirectly, of a national firearms or ammunition registry; or\n**(2)**\ninterfere with the authority of a State, under section 927 of title 18, United States Code, to enact a law on the same subject matter as this Act.\n#### 5. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3873",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Jaime\u2019s Law",
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
        "updateDate": "2026-03-09T18:37:51Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7564ih.xml"
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
      "title": "Jaime\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T07:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Jaime\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T07:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent the purchase of ammunition by prohibited purchasers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T07:48:29Z"
    }
  ]
}
```
