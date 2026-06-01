# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2650?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2650
- Title: End Gun Violence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2650
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-04-14T19:46:26Z
- Update date including text: 2026-04-14T19:46:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2650",
    "number": "2650",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "End Gun Violence Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T19:46:26Z",
    "updateDateIncludingText": "2026-04-14T19:46:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:03:20Z",
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
      "sponsorshipDate": "2025-04-03",
      "state": "MA"
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
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-07",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2650ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2650\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Neguse (for himself, Mr. Auchincloss , Ms. Kelly of Illinois , and Ms. Dean of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit the sale or other disposition of any firearm or ammunition to any person who has been convicted of a violent misdemeanor, and for other purposes.\n#### 1. Short title\nThis Act may be referred to as the End Gun Violence Act of 2025 .\n#### 2. Prohibition on sale or other disposition of a firearm or ammunition to a person convicted of a violent misdemeanor\nSection 922(d) of title 18, United States Code, is amended in the 1st sentence\u2014\n**(1)**\nin paragraph (10), by striking or at the end;\n**(2)**\nin paragraph (11), by striking the period and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(12) has been convicted in any court of a violent misdemeanor within the preceding 5 years. .\n#### 3. Definition of violent misdemeanor\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(38) (A) The term violent misdemeanor means an offense that\u2014 (i) is a misdemeanor under Federal, State, tribal, or local law; and (ii) has as an element\u2014 (I) the use, attempted use, or threatened use of\u2014 (aa) physical force; or (bb) a deadly weapon; (II) the intent to cause physical injury; or (III) knowingly causing physical injury. (B) (i) A person shall not be considered to have been convicted of such an offense for purposes of this chapter, unless\u2014 (I) the person was represented by counsel in the case, or knowingly and intelligently waived the right to counsel in the case; and (II) in the case of a prosecution for an offense described in this paragraph for which a person was entitled to a jury trial in the jurisdiction in which the case was tried, either\u2014 (aa) the case was tried by a jury, or (bb) the person knowingly and intelligently waived the right to have the case tried by a jury, by guilty plea or otherwise. (ii) A person shall not be considered to have been convicted of such an offense for purposes of this chapter if the conviction has been expunged or set aside, or is an offense for which the person has been pardoned or has had civil rights restored (if the law of the applicable jurisdiction provides for the loss of civil rights under such an offense) unless the pardon, expungement, or restoration of civil rights expressly provides that the person may not ship, transport, possess, or receive firearms. .\n#### 4. Conforming amendments\n##### (a)\nParagraphs (1)(B)(ii), (2), (4), and (5) of section 922(t) of title 18, United States Code, are each amended by striking receipt and all that follows through subsection (g) and inserting knowing sale or disposition of a firearm by the licensee to such other person, or the receipt of a firearm by such other person would violate subsection (d), (g), .\n##### (b)\nSection 923(d)(1)(B) of such title is amended by striking section 922(g) and (n) of this chapter and inserting subsection (g) or (n) of section 922, and is not a person to whom the knowing sale or disposition of a firearm or ammunition is prohibited by section 922(d) .\n##### (c)\nSection 925A of such title is amended in paragraph (2), by inserting and to whom the knowing sale or disposition of a firearm was not prohibited pursuant to subsection (d) of such section after section 922 .\n##### (d)\nSection 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) is amended\u2014\n**(1)**\nin subsection (e)(1)\u2014\n**(A)**\nin subparagraph (A), by striking for whom and all that follows through subsection (g) and inserting to whom the knowing sale or disposition of a firearm, or for whom receipt of a firearm, would violate subsection (d), (g), ; and\n**(B)**\nin each of subparagraphs (F)(iii)(I) and (G)(i), by striking (g) and inserting (d), (g), ;\n**(2)**\nin subsection (g), by striking receipt of a firearm by a prospective transferee would violate subsection (g) and inserting the knowing sale or disposition of a firearm to, or the possession or receipt of a firearm by, a prospective transferee would violate subsection (d), (g), ; and\n**(3)**\nin subsection (i)(2), by striking prohibited by section 922 (g) or (n) of title 18, United States Code or State law, from receiving a firearm. and inserting to whom the knowing sale or disposition of, or for whom the possession or receipt of, a firearm is prohibited by subsection (d), (g), or (n) of section 922 of title 18, United States Code, or State law. .\n##### (e)\nSection 101(b) of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40911(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(A), by striking a person is disqualified from possessing or receiving a firearm under subsection (g) and inserting the knowing sale or disposition of a firearm to, or the possession or receipt of a firearm by, a person is prohibited under subsection (d), (g), ; and\n**(2)**\nin paragraph (2)(A), by striking a member of the Armed Forces involved in such proceeding is disqualified from possessing or receiving a firearm under subsection (g) and inserting the knowing sale or disposition of a firearm to, or the possession or receipt of a firearm by, a member of the Armed Forces is prohibited under subsection (d), (g), .\n##### (f)\nSection 102 of the NICS Improvement Amendments Act of 2007 ( 34 U.S.C. 40912 ) is amended\u2014\n**(1)**\nin subsection (b)(3)\u2014\n**(A)**\nby inserting , or to whom the knowing sale or disposition of a firearm is prohibited, after firearm ; and\n**(B)**\nby striking subsection (g) and inserting subsection (d), (g), ; and\n**(2)**\nin subsection (c)(1)(A), by inserting , or is a person to whom the knowing sale or disposition of a firearm is prohibited by subsection (d) of such section before the period.\n#### 5. Applicability\nThe amendments made by this Act shall not apply with respect to convictions occurring before the date that is 6 months after the date of enactment of this Act.\n#### 6. Rule of construction\nNothing in this Act shall\u2014\n**(1)**\nalter the requirements of subsections (d)(8) or (g)(8) of section 922 of title 18, United States Code; or\n**(2)**\nhave a limiting effect on State, tribal, or local law.",
      "versionDate": "2025-04-03",
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
        "updateDate": "2025-05-01T13:26:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2650",
          "measure-number": "2650",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2650v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>End Gun Violence Act of 2025</strong></p><p>This bill extends federal restrictions on the sale or disposition of firearms and ammunition to a new category of persons: persons who have been convicted in any court of a violent misdemeanor within the preceding five years.</p><p>\u00a0</p>"
        },
        "title": "End Gun Violence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2650.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Gun Violence Act of 2025</strong></p><p>This bill extends federal restrictions on the sale or disposition of firearms and ammunition to a new category of persons: persons who have been convicted in any court of a violent misdemeanor within the preceding five years.</p><p>\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr2650"
    },
    "title": "End Gun Violence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>End Gun Violence Act of 2025</strong></p><p>This bill extends federal restrictions on the sale or disposition of firearms and ammunition to a new category of persons: persons who have been convicted in any court of a violent misdemeanor within the preceding five years.</p><p>\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr2650"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2650ih.xml"
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
      "title": "End Gun Violence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Gun Violence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit the sale or other disposition of any firearm or ammunition to any person who has been convicted of a violent misdemeanor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:38Z"
    }
  ]
}
```
