# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1312?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1312
- Title: No Asylum for Criminals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1312
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-04T01:46:44Z
- Update date including text: 2026-03-04T01:46:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1312",
    "number": "1312",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Asylum for Criminals Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T01:46:44Z",
    "updateDateIncludingText": "2026-03-04T01:46:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:00:35Z",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SC"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TN"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1312ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1312\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Harris of North Carolina (for himself, Ms. Mace , Mr. Weber of Texas , Mr. Moore of Alabama , Mr. Stutzman , Mr. Edwards , Mr. Self , Mr. Biggs of Arizona , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide that an alien who has been convicted of a crime is ineligible for asylum, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Asylum for Criminals Act of 2025 .\n#### 2. Aliens convicted of crimes ineligible for asylum\nClause (ii) of section 208(b)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1158 ) is amended\u2014\n**(1)**\nby amending clause (ii) of subparagraph (A) to read as follows:\n(ii) except as provided in subparagraph (B), the alien has been finally convicted of a felony or misdemeanor; ;\n**(2)**\nby amending subparagraph (B) to read as follows:\n(B) Exception The Secretary of Homeland Security may designate by regulation political offenses committed outside the United States that will be not considered to be a crime described in clause (ii). The authority under this subparagraph is limited to political offenses committed outside the United States. ; and\n**(3)**\nby adding at the end the following:\n(E) Definitions In this paragraph: (i) The term felony means\u2014 (I) any crime defined as a felony by the relevant jurisdiction (Federal, State, tribal, or local) of conviction; or (II) any crime punishable by more than one year of imprisonment. (ii) The term misdemeanor means\u2014 (I) any crime defined as a misdemeanor by the relevant jurisdiction (Federal, State, tribal, or local) of conviction; or (II) any crime not punishable by more than one year of imprisonment. .",
      "versionDate": "2025-02-13",
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
        "name": "Immigration",
        "updateDate": "2025-03-18T14:09:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1312",
          "measure-number": "1312",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1312v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Asylum for Criminals Act of 2025 </strong></p><p>This bill bars an individual who has been convicted of a felony or misdemeanor from receiving asylum, with limited exceptions. Specifically, the Department of Homeland Security may designate political offenses committed outside of the United States that shall not be considered a crime for this purpose.</p><p>Currently, an individual shall be barred from receiving asylum for only certain types of criminal convictions, such as if the individual is convicted for (1) an aggravated felony, or (2) a particularly serious crime and as a result deemed a danger to the United States.</p>"
        },
        "title": "No Asylum for Criminals Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1312.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Asylum for Criminals Act of 2025 </strong></p><p>This bill bars an individual who has been convicted of a felony or misdemeanor from receiving asylum, with limited exceptions. Specifically, the Department of Homeland Security may designate political offenses committed outside of the United States that shall not be considered a crime for this purpose.</p><p>Currently, an individual shall be barred from receiving asylum for only certain types of criminal convictions, such as if the individual is convicted for (1) an aggravated felony, or (2) a particularly serious crime and as a result deemed a danger to the United States.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1312"
    },
    "title": "No Asylum for Criminals Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Asylum for Criminals Act of 2025 </strong></p><p>This bill bars an individual who has been convicted of a felony or misdemeanor from receiving asylum, with limited exceptions. Specifically, the Department of Homeland Security may designate political offenses committed outside of the United States that shall not be considered a crime for this purpose.</p><p>Currently, an individual shall be barred from receiving asylum for only certain types of criminal convictions, such as if the individual is convicted for (1) an aggravated felony, or (2) a particularly serious crime and as a result deemed a danger to the United States.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1312"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1312ih.xml"
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
      "title": "No Asylum for Criminals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Asylum for Criminals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to provide that an alien who has been convicted of a crime is ineligible for asylum, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:28Z"
    }
  ]
}
```
