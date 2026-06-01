# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1894
- Title: FISH Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1894
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-09-03T08:05:56Z
- Update date including text: 2025-09-03T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1894",
    "number": "1894",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "FISH Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-03T08:05:56Z",
    "updateDateIncludingText": "2025-09-03T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1894ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1894\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Calvert (for himself, Mr. Costa , Mr. LaMalfa , Mr. McClintock , and Mr. Issa ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to vest in the Secretary of the Interior functions under that Act with respect to species of fish that spawn in fresh or estuarine waters and migrate to ocean waters and species of fish that spawn in ocean waters and migrate to fresh or estuarine waters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federally Integrated Species Health Act of 2025 or the FISH Act of 2025 .\n#### 2. Transfer of functions with respect to anadromous species and catadromous species\n##### (a) Transfer of functions\nAll functions with respect to anadromous species and catadromous species under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) that were vested in the Secretary of Commerce or the National Marine Fisheries Service immediately before the enactment of this Act are transferred to the Secretary of the Interior.\n##### (b) Conforming amendments\nThe Endangered Species Act of 1973 is amended\u2014\n**(1)**\nin section 3(15) ( 16 U.S.C. 1532(15) )\u2014\n**(A)**\nby inserting (A) after (15) ; and\n**(B)**\nby inserting after Secretary of Agriculture. the following:\n(B) Notwithstanding subparagraph (A), with respect to anadromous species and catadromous species, the term Secretary means the Secretary of the Interior. ; and\n**(2)**\nin section 3 ( 16 U.S.C. 1532 ) by adding at the end the following:\n(22) The term anadromous species means a species of fish that spawns in fresh or estuarine waters and migrates to ocean waters. (23) The term catadromous species means a species of fish that spawns in ocean waters and migrates to fresh or estuarine waters. .\n##### (c) Reconsideration of administrative determinations\nFollowing the complete transfer of National Marine Fisheries Service responsibilities to the Department of the Interior, any final administrative determination made by National Marine Fisheries Service within 3 years prior to the date of the transfer may be reconsidered upon request to the Secretary of the Interior. The Secretary may grant or deny the request, and the final decision will be made publicly available. Any request for reconsideration made under this subsection shall be filed with the Department of Interior within 365 days of transfer completion.\n#### 3. Miscellaneous provisions\n##### (a) References\nAny reference in any other Federal law, Executive order, rule, regulation, or delegation of authority, or any document of or pertaining to a department or office from which a function is transferred by this Act\u2014\n**(1)**\nto the head of such department or office is deemed to refer to the Secretary of the Interior; or\n**(2)**\nto such department or office is deemed to refer to the Department of the Interior.\n##### (b) Exercise of authorities\nExcept as otherwise provided by law, the Secretary of the Interior may, for purposes of performing the functions transferred by this Act, exercise all authorities under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) that were available with respect to the performance of that function immediately before the effective date of the transfer of the function under this Act.\n##### (c) Savings provisions\n**(1) Legal documents**\nAll orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges\u2014\n**(A)**\nthat have been issued, made, granted, or allowed to become effective by the Secretary of Commerce, any officer or employee of the Department of Commerce, or any other Government official in the performance of any function that is transferred by this Act, or by a court of competent jurisdiction with respect to such performance; and\n**(B)**\nthat are in effect on the effective date of this Act (or become effective after such date pursuant to their terms as in effect on such effective date),\nshall continue in effect according to their terms until modified, terminated, superseded, set aside, or revoked in accordance with law by the President, any other authorized official, a court of competent jurisdiction, or operation of law.\n**(2) Proceedings**\n**(A) In general**\nThis Act shall not affect any proceedings or any application for any benefits, service, license, permit, certificate, or financial assistance pending on the date of the enactment of this Act before an office transferred by this Act. Such proceedings and applications shall be continued. Orders shall be issued in such proceedings, appeals shall be taken therefrom, and payments shall be made pursuant to such orders, as if this Act had not been enacted, and orders issued in any such proceeding shall continue in effect until modified, terminated, superseded, or revoked by a duly authorized official, by a court of competent jurisdiction, or by operation of law.\n**(B) Limitation**\nNothing in this paragraph shall be considered to prohibit the discontinuance or modification of any such proceeding under the same terms and conditions and to the same extent that such proceeding could have been discontinued or modified if this Act had not been enacted.\n**(3) Suits**\nThis Act shall not affect suits commenced before the date of the enactment of this Act, and in all such suits, proceeding shall be had, appeals taken, and judgments rendered in the same manner and with the same effect as if this Act had not been enacted.\n**(4) Nonabatement of actions**\nNo suit, action, or other proceeding commenced by or against the Department of Commerce or the Secretary of Commerce, or by or against any individual in the official capacity of such individual as an officer or employee of the Department of Commerce, shall abate by reason of the enactment of this Act.\n**(5) Continuance of suits**\nIf any Government officer in the official capacity of such officer is party to a suit with respect to a function of the officer, and under this Act such function is transferred to any other officer or office, then such suit shall be continued with the other officer or the head of such other office, as applicable, substituted or added as a party.\n**(6) Administrative procedure and judicial review**\nExcept as otherwise provided by this Act, any statutory requirements relating to notice, hearings, action upon the record, or administrative or judicial review that apply to any function transferred by this Act shall apply to the exercise of such function by the head of the Federal agency, and other officers of the agency, to which such function is transferred by this Act.\n#### 4. Definitions\nFor purposes of this Act:\n**(1) Anadromous species and catadromous species**\nEach of the terms anadromous species and catadromous species has the meaning that term has under section 3 of the Endangered Species Act of 1973 ( 16 U.S.C. 1532 ), as amended by section 3 of this Act.\n**(2) Function**\nThe term function includes any duty, obligation, power, authority, responsibility, right, privilege, activity, or program.\n**(3) Office**\nThe term office includes any office, administration, agency, bureau, institute, council, unit, organizational entity, or component thereof.",
      "versionDate": "2025-03-06",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-20T13:10:08Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1894ih.xml"
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
      "title": "FISH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FISH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federally Integrated Species Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to vest in the Secretary of the Interior functions under that Act with respect to species of fish that spawn in fresh or estuarine waters and migrate to ocean waters and species of fish that spawn in ocean waters and migrate to fresh or estuarine waters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:23Z"
    }
  ]
}
```
