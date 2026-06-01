# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4235
- Title: To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act.
- Congress: 119
- Bill type: HR
- Bill number: 4235
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-05-18T20:36:53Z
- Update date including text: 2026-05-18T20:36:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4235",
    "number": "4235",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act.",
    "type": "HR",
    "updateDate": "2026-05-18T20:36:53Z",
    "updateDateIncludingText": "2026-05-18T20:36:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:00:35Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NY"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "MD"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "NH"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "WI"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NY"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "DC"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "TN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DE"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "TX"
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
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "TN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "VA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4235ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4235\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Ms. Lee of Florida (for herself, Mr. Nadler , Mr. Raskin , Ms. Goodlander , and Mr. Fitzgerald ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act.\n#### 1. Holocaust Expropriated Art Recovery Act of 2016 improvements\n##### (a) In general\nThe Holocaust Expropriated Art Recovery Act of 2016 ( 22 U.S.C. 1621 note) is amended\u2014\n**(1)**\nin section 2\u2014\n**(A)**\nby redesignating paragraph (8) as paragraph (10);\n**(B)**\nby inserting after paragraph (7) the following:\n(8) The intent of this Act is to permit claims to recover Nazi-looted art to be brought, notwithstanding the passage of time since World War II. Some courts have frustrated the intent of this Act by dismissing recovery lawsuits in reliance on defenses based on the passage of time, such as laches (for example, Zuckerman v Metropolitan Museum of Art, 928 F.3d 186 (2d Cir. 2019)) or adverse possession, acquisitive prescription, or usucapion (for example, Cassirer v. Thyssen-Bornemisza Foundation, 89 F.4th 1226 (9th Cir. 2024)) or on other non-merits discretionary defenses, such as the act of state doctrine (for example, Von Saher v Norton Simon Museum, 897 F.3d 1141 (9th Cir. 2018)), forum non-conveniens, international comity, or prudential exhaustion. In order to effectuate the purpose of the Act to permit claims to recover Nazi-looted art to be resolved on the merits, these defenses must be precluded. (9) This Act also is intended to allow claims in accordance with the procedures under this Act for the recovery of artwork or other property lost during the covered period because of Nazi persecution, regardless of the nationality or citizenship of the alleged victim, notwithstanding the domestic takings rule under Federal Republic of Germany v. Philipp, 592 U.S. 169 (2021). ; and\n**(C)**\nin paragraph (10), as so redesignated, by striking will yield just and fair resolutions in a more efficient and predictable manner and inserting may, in some circumstances, yield just and fair resolutions as well ;\n**(2)**\nin section 3(2), by inserting and other non-merits defenses after statutes of limitation ;\n**(3)**\nin section 5\u2014\n**(A)**\nby striking subsection (g);\n**(B)**\nby redesignating subsections (e) and (f) as subsections (h) and (i), respectively;\n**(C)**\nby redesignating subsections (b), (c), and (d) as subsections (c), (d), and (e), respectively;\n**(D)**\nby inserting after subsection (a) the following:\n(b) Relation to foreign state immunities Notwithstanding any other law or prior judicial decision, any civil claim or cause of action covered by subsection (a) shall be deemed to be an action in which rights in violation of international law are in issue for purposes of 1605(a)(3) of title 28, United States Code, without regard to the nationality or citizenship of the alleged victim. ;\n**(E)**\nin subsection (d), as so redesignated, in the matter preceding paragraph (1), by striking subsection (e) and inserting subsection (h) ;\n**(F)**\nin subsection (e), as so redesignated\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking Subsection (a) and inserting Subsections (a), (b), (f), and (g) ; and\n**(ii)**\nin paragraph (2), by striking during the period and all that follows and inserting on or after the date of enactment of this Act. ; and\n**(G)**\nby inserting after subsection (e), as so redesignated, the following:\n(f) Defenses based on passage of time and other non-Merits defenses With respect to any claim that is otherwise timely under this Act\u2014 (1) all defenses or substantive doctrines based on the passage of time, including laches, adverse possession, acquisitive prescription, and usucapion, may not be applied with respect to the claim; and (2) all non-merits discretionary bases for dismissal, including the act of state doctrine, international comity, forum non-conveniens, prudential exhaustion, and similar doctrines unrelated to the merits, may not be applied with respect to the claim. (g) Nationwide service of process For a civil action brought under subsection (a) in any State or Federal court, process may be served in the judicial district where the case is brought or any other judicial district of the United States where the defendant may be found, resides, has an agent, or transacts business. ; and\n**(4)**\nby adding at the end the following:\n6. Severability If any provision of this Act, or the application of a provision of this Act to any person or circumstance, is held invalid, the remainder of this Act, and the application of such provision to other persons and circumstances, shall not be affected thereby. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to any civil claim or cause of action that is\u2014\n**(1)**\npending in any court on the date of enactment of this Act, including any civil claim or cause of action that is pending on appeal or for which the time to file an appeal has not expired; or\n**(2)**\nfiled on or after the date of enactment of this Act.",
      "versionDate": "2025-06-27",
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
        "actionDate": "2026-04-13",
        "text": "Became Public Law No: 119-82."
      },
      "number": "1884",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Holocaust Expropriated Art Recovery Act of 2025",
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
            "name": "Art, artists, authorship",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2025-12-15T20:36:09Z"
          },
          {
            "name": "World history",
            "updateDate": "2025-12-15T20:36:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-09-19T15:02:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-27",
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
          "measure-id": "id119hr4235",
          "measure-number": "4235",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-27",
          "originChamber": "HOUSE",
          "update-date": "2026-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4235v00",
            "update-date": "2026-03-18"
          },
          "action-date": "2025-06-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong>This bill permanently extends and expands judicial authority under the Holocaust Expropriated Art Recovery Act of 2016. The law allows and establishes procedures for civil claims and causes of action to recover artwork and other property lost between 1933 and 1945 because of Nazi persecution.</p><p>Among the changes, the bill removes the deadline for filing civil claims or causes of action. Currently, the filing deadline is December 31, 2026. (Claims must still be filed within six years of the claimant's discovery of the property in question.)</p><p>The bill permits courts to exercise jurisdiction over civil claims or causes of action against a foreign state without regard to the nationality or citizenship of the alleged victim. The art or property at issue must still have a connection to the foreign state's commercial activities in the United States.</p><p>Additionally, the bill authorizes nationwide service of process, which allows courts to exercise personal jurisdiction over defendants in any judicial district where they may be found, reside, have an agent, or transact business.</p><p>Finally, the bill limits the defenses that may be asserted against civil claims or causes of action, including by prohibiting</p><ul><li>defenses based on the passage of time, including equitable defenses such as laches (i.e., unreasonable delays); and</li><li>discretionary bases for dismissal that are unrelated to the merits of the claim, including international comity\u00a0(i.e., deference to the laws of other countries).</li></ul><p>These changes apply to pending and future civil claims or causes of action.</p>"
        },
        "title": "To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4235.xml",
    "summary": {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill permanently extends and expands judicial authority under the Holocaust Expropriated Art Recovery Act of 2016. The law allows and establishes procedures for civil claims and causes of action to recover artwork and other property lost between 1933 and 1945 because of Nazi persecution.</p><p>Among the changes, the bill removes the deadline for filing civil claims or causes of action. Currently, the filing deadline is December 31, 2026. (Claims must still be filed within six years of the claimant's discovery of the property in question.)</p><p>The bill permits courts to exercise jurisdiction over civil claims or causes of action against a foreign state without regard to the nationality or citizenship of the alleged victim. The art or property at issue must still have a connection to the foreign state's commercial activities in the United States.</p><p>Additionally, the bill authorizes nationwide service of process, which allows courts to exercise personal jurisdiction over defendants in any judicial district where they may be found, reside, have an agent, or transact business.</p><p>Finally, the bill limits the defenses that may be asserted against civil claims or causes of action, including by prohibiting</p><ul><li>defenses based on the passage of time, including equitable defenses such as laches (i.e., unreasonable delays); and</li><li>discretionary bases for dismissal that are unrelated to the merits of the claim, including international comity\u00a0(i.e., deference to the laws of other countries).</li></ul><p>These changes apply to pending and future civil claims or causes of action.</p>",
      "updateDate": "2026-03-18",
      "versionCode": "id119hr4235"
    },
    "title": "To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act."
  },
  "summaries": [
    {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill permanently extends and expands judicial authority under the Holocaust Expropriated Art Recovery Act of 2016. The law allows and establishes procedures for civil claims and causes of action to recover artwork and other property lost between 1933 and 1945 because of Nazi persecution.</p><p>Among the changes, the bill removes the deadline for filing civil claims or causes of action. Currently, the filing deadline is December 31, 2026. (Claims must still be filed within six years of the claimant's discovery of the property in question.)</p><p>The bill permits courts to exercise jurisdiction over civil claims or causes of action against a foreign state without regard to the nationality or citizenship of the alleged victim. The art or property at issue must still have a connection to the foreign state's commercial activities in the United States.</p><p>Additionally, the bill authorizes nationwide service of process, which allows courts to exercise personal jurisdiction over defendants in any judicial district where they may be found, reside, have an agent, or transact business.</p><p>Finally, the bill limits the defenses that may be asserted against civil claims or causes of action, including by prohibiting</p><ul><li>defenses based on the passage of time, including equitable defenses such as laches (i.e., unreasonable delays); and</li><li>discretionary bases for dismissal that are unrelated to the merits of the claim, including international comity\u00a0(i.e., deference to the laws of other countries).</li></ul><p>These changes apply to pending and future civil claims or causes of action.</p>",
      "updateDate": "2026-03-18",
      "versionCode": "id119hr4235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4235ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-15T02:18:23Z"
    },
    {
      "title": "To clarify the Holocaust Expropriated Art Recovery Act of 2016, to appropriately limit the application of defenses based on the passage of time and other non-merits defenses to claims under that Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:30Z"
    }
  ]
}
```
