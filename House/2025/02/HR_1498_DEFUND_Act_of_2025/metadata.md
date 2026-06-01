# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1498?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1498
- Title: DEFUND Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1498
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-01-17T01:30:54Z
- Update date including text: 2026-01-17T01:30:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1498",
    "number": "1498",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "DEFUND Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-17T01:30:54Z",
    "updateDateIncludingText": "2026-01-17T01:30:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:35:25Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TN"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "WY"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "OK"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "KY"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "AL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "UT"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "ID"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1498ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1498\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Roy (for himself, Mr. Crane , Mrs. Harshbarger , Mrs. Luna , Ms. Hageman , Mr. Brecheen , Mr. Massie , Ms. Greene of Georgia , and Mr. Rogers of Alabama ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo terminate membership by the United States in the United Nations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disengaging Entirely From the United Nations Debacle Act of 2025 or the DEFUND Act of 2025 .\n#### 2. Repeal of United Nations Participation Act of 1945\n##### (a) Repeal\nThe United Nations Participation Act of 1945 ( Public Law 79\u2013264 ; 22 U.S.C. 287 et seq. ) is repealed.\n##### (b) Termination of membership in United Nations\nThe President shall terminate all membership by the United States in the United Nations, and in any organ, specialized agency, commission, or other formally affiliated body of the United Nations.\n##### (c) Closure of United States Mission to United Nations\nThe United States Mission to the United Nations is closed. Any remaining functions of such office shall not be carried out.\n#### 3. Repeal of United Nations Headquarters Agreement Act\n##### (a) Repeal\nThe Joint Resolution of August 4, 1947 (61 Stat. 756, chapter 482; 22 U.S.C. 287 note) (commonly known as the United Nations Headquarters Agreement Act ) is repealed.\n##### (b) Withdrawal\nThe United States withdraws from the agreement between the United States of America and the United Nations regarding the headquarters of the United Nations (signed at Lake Success, New York, on June 26, 1947, which was brought into effect by the United Nations Headquarters Agreement Act).\n#### 4. United States assessed and voluntary contributions to the United Nations\nNo funds are authorized to be appropriated or otherwise made available for assessed or voluntary contributions of the United States to the United Nations or to any organ, specialized agency, commission or other formally affiliated body of the United Nations, except that funds may be appropriated to facilitate termination of United States membership and withdrawal of United States personnel and equipment, in accordance with sections 2 and 3, respectively. Upon termination of United States membership, no payments shall be made to the United Nations or to any organ, specialized agency, commission or other formally affiliated body of the United Nations, out of any funds appropriated prior to such termination or out of any other funds available for such purposes.\n#### 5. United Nations peacekeeping operations\nThe United States may not participate in any peacekeeping operation of the United Nations.\n#### 6. Withdrawal of United Nations presence in facilities of the Government of the United States and repeal of diplomatic immunity\n##### (a) Withdrawal from United States Government property\nThe United Nations (including any organ, specialized agency, commission or other formally affiliated body of the United Nations) may not occupy or use any property or facility of the United States Government.\n##### (b) Diplomatic immunity\nNo officer or employee of the United Nations (including any organ, specialized agency, commission or other formally affiliated body of the United Nations) or any representative, officer, or employee of any mission to the United Nations of any foreign government shall be entitled to enjoy the privileges and immunities of the Vienna Convention on Diplomatic Relations done at Vienna April 18, 1961, nor may any such privileges and immunities be extended to any such individual. The privileges, exemptions, and immunities provided for in the International Organizations Immunities Act ( 22 U.S.C. 288 et seq. ), or in any agreement or treaty to which the United States is a party, including the Agreement Between the United Nations and the United States of America Regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, and the Convention on the Privileges and Immunities of the United Nations, done at New York February 13, 1946, and entered into force with respect to the United States on April 29, 1970, shall not apply to the United Nations or to any organ, specialized agency, commission or other formally affiliated body of the United Nations, to the officers and employees of the United Nations, or of any organ, specialized agency, commission or other formally affiliated body of the United Nations, or to the families, suites, or servants of such officers or employees.\n#### 7. Repeal of United States participation in the World Health Organization\nThe joint resolution entitled Joint Resolution providing for membership and participation by the United States in the World Health Organization and authorizing an appropriation therefor , approved June 14, 1948 ( 22 U.S.C. 290 ), is repealed.\n#### 8. Repeal of involvement in United Nations conventions and agreements\nThe United States shall end any participation in any conventions and agreements with the United Nations and any organ, specialized agency, commission, or other formally affiliated body of the United Nations. Any remaining functions of such conventions and agreements shall not be carried out.\n#### 9. Prohibition on United States reentry into United Nations\n##### (a) In general\nThe President may not enter into an agreement for membership in the United Nations or any organ, specialized agency, commission, or other formally affiliated body of the United Nations without the advice and consent of the Senate.\n##### (b) Withdrawal provision requirement\nThe advice and consent of the Senate to the ratification of any agreement seeking membership in the United Nations or any organ, specialized agency, commission, or other formally affiliated body of the United Nations shall be subject to a reservation, which shall be included in the instrument of ratification, that reserves the right of the United States to withdraw from such agreement.\n#### 10. Notification\nThe Secretary of State shall notify the United Nations and any organ, specialized agency, commission, or other formally affiliated body of the United Nations of the provisions of this Act.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "669",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DEFUND Act of 2025",
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
        "updateDate": "2025-05-09T15:23:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1498",
          "measure-number": "1498",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2026-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1498v00",
            "update-date": "2026-01-17"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disengaging Entirely From the United Nations Debacle Act of 2025 or the DEFUND Act of 2025</strong></p><p>This bill directs the President to terminate U.S. membership in the United Nations (U.N.) and all formally affiliated bodies. It also ends U.S. participation in all U.N. conventions and agreements.</p><p>Funds may be appropriated to facilitate U.S. withdrawal from the U.N. No funds may be made available for contributions or payments to any U.N. body.</p><p>The bill prohibits U.S. participation in any U.N. peacekeeping operation.</p><p>The bill also repeals diplomatic immunity for officers and employees of the U.N. and for officers and employees of foreign government missions to the U.N.</p><p>The bill repeals various acts related to the U.N., including the United Nations Participation Act of 1945, the United Nations Headquarters Agreement Act, and a joint resolution establishing U.S. membership in the World Health Organization.</p><p>The United States may not rejoin the U.N. or any formally affiliated body without the advice and consent of the Senate. Any agreement to rejoin the U.N. or a formally affiliated body must include the right of the United States to withdraw from the agreement.</p>"
        },
        "title": "DEFUND Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1498.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disengaging Entirely From the United Nations Debacle Act of 2025 or the DEFUND Act of 2025</strong></p><p>This bill directs the President to terminate U.S. membership in the United Nations (U.N.) and all formally affiliated bodies. It also ends U.S. participation in all U.N. conventions and agreements.</p><p>Funds may be appropriated to facilitate U.S. withdrawal from the U.N. No funds may be made available for contributions or payments to any U.N. body.</p><p>The bill prohibits U.S. participation in any U.N. peacekeeping operation.</p><p>The bill also repeals diplomatic immunity for officers and employees of the U.N. and for officers and employees of foreign government missions to the U.N.</p><p>The bill repeals various acts related to the U.N., including the United Nations Participation Act of 1945, the United Nations Headquarters Agreement Act, and a joint resolution establishing U.S. membership in the World Health Organization.</p><p>The United States may not rejoin the U.N. or any formally affiliated body without the advice and consent of the Senate. Any agreement to rejoin the U.N. or a formally affiliated body must include the right of the United States to withdraw from the agreement.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr1498"
    },
    "title": "DEFUND Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disengaging Entirely From the United Nations Debacle Act of 2025 or the DEFUND Act of 2025</strong></p><p>This bill directs the President to terminate U.S. membership in the United Nations (U.N.) and all formally affiliated bodies. It also ends U.S. participation in all U.N. conventions and agreements.</p><p>Funds may be appropriated to facilitate U.S. withdrawal from the U.N. No funds may be made available for contributions or payments to any U.N. body.</p><p>The bill prohibits U.S. participation in any U.N. peacekeeping operation.</p><p>The bill also repeals diplomatic immunity for officers and employees of the U.N. and for officers and employees of foreign government missions to the U.N.</p><p>The bill repeals various acts related to the U.N., including the United Nations Participation Act of 1945, the United Nations Headquarters Agreement Act, and a joint resolution establishing U.S. membership in the World Health Organization.</p><p>The United States may not rejoin the U.N. or any formally affiliated body without the advice and consent of the Senate. Any agreement to rejoin the U.N. or a formally affiliated body must include the right of the United States to withdraw from the agreement.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr1498"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1498ih.xml"
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
      "title": "DEFUND Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DEFUND Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disengaging Entirely From the United Nations Debacle Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To terminate membership by the United States in the United Nations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:34Z"
    }
  ]
}
```
