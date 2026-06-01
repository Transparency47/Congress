# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2511
- Title: Sarah Katz Caffeine Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 2511
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-03-31T08:05:35Z
- Update date including text: 2026-03-31T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2511",
    "number": "2511",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Sarah Katz Caffeine Safety Act",
    "type": "HR",
    "updateDate": "2026-03-31T08:05:35Z",
    "updateDateIncludingText": "2026-03-31T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "WA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2026-03-30",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2511\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mr. Menendez (for himself, Mr. Smith of New Jersey , Ms. Schrier , Mr. Veasey , Mr. Carter of Louisiana , Ms. Norton , Mrs. McIver , Mrs. Watson Coleman , Mr. Sherman , Mr. Kennedy of New York , Ms. Tlaib , Mr. Deluzio , Mr. Goldman of New York , and Ms. Underwood ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to establish certain labeling requirements for caffeine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sarah Katz Caffeine Safety Act .\n#### 2. Caffeine labeling requirements\n##### (a) Information required To be disclosed by restaurants and retail food establishments\n**(1) In general**\nSection 403(q)(5)(H) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(q)(5)(H) ) is amended\u2014\n**(A)**\nby amending subclause (i) to read as follows:\n(i) General requirements for restaurants and similar retail food establishments (I) Standard menu items Except for food described in subclause (vii), in the case of food that is a standard menu item that is offered for sale in a restaurant or similar retail food establishment that is part of a chain with 20 or more locations doing business under the same name (regardless of the type of ownership of the locations) and offering for sale substantially the same menu items, the restaurant or similar retail food establishment shall disclose the information described in subclauses (ii) and (iii). (II) Temporary menu items (aa) In general In the case of food that is a temporary menu item that is offered for sale in a restaurant or similar retail food establishment that is part of a chain with 20 or more locations doing business under the same name (regardless of the type of ownership of the locations) and offering for sale substantially the same menu items, the restaurant or similar retail food establishment shall disclose the information described in subclause (ii)(III). (bb) Temporary menu item defined In this item, the term temporary menu item means a food that appears on a menu or menu board for less than a total of 60 days per calendar year. The 60 days includes the total of consecutive and non-consecutive days the item appears on the menu. ;\n**(B)**\nin subclause (ii)\u2014\n**(i)**\nby redesignating items (III) and (IV) as items (IV) and (V), respectively, and moving the margins of such items 2 ems to the right;\n**(ii)**\nby inserting after item (II) the following:\n(III) in the case of a standard menu item or temporary menu item that contains any added caffeine (as the Secretary shall by regulation define) and at least 150 milligrams of total caffeine per serving, the statement \u2018High caffeine\u2019, or such other similar statement or symbol as the Secretary determines appropriate, adjacent to the name of the standard menu item or temporary menu item, so as to be clearly associated with such menu item, on the menu listing the item for sale and on the menu board, including a drive through menu board; ; and\n**(iii)**\nin item (IV) (as so redesignated), by inserting before the semicolon the following: and the number of milligrams of caffeine in the item ; and\n**(C)**\nin subclause (vii)(I), by striking Subclauses (i) through (vi) and inserting Subject to subclause (i)(II), subclauses (i) through (vi) .\n**(2) Conforming amendments**\nSection 403(q)(5) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343(q)(5) ) is amended\u2014\n**(A)**\nin clause (A)\u2014\n**(i)**\nin subclause (i), by striking clause (H)(ii)(III) and inserting clause (H)(ii)(IV) ; and\n**(ii)**\nin subclause (ii), by striking clause (H)(ii)(III) and inserting clause (H)(ii)(IV) ; and\n**(B)**\nin clause (H)\u2014\n**(i)**\nin subclause (ii)(V) (as redesignated by subsection (a)(1)(B)(i) of this section), by striking item (III) and inserting item (IV) ;\n**(ii)**\nin subclause (vi), by striking subclause (ii)(III) each place it appears and inserting subclause (ii)(IV) ; and\n**(iii)**\nin subclause (vii)(II), by striking subclauses (ii)(III) and (vi) and inserting subclauses (ii)(IV) and (vi) .\n##### (b) Caffeine labeling requirements for food and dietary supplements\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If it is a food (including a dietary supplement) that contains more than 10 milligrams of caffeine, unless the label of such food includes\u2014 (1) the number of milligrams of caffeine in the food; (2) a statement of whether the caffeine in the food is naturally occurring or an additive; and (3) an advisory statement indicating that the daily recommended limit of caffeine for healthy adults is 400 milligrams (or such other limit as the Secretary determines appropriate). .\n#### 3. FDA and NIH reviews of safety of caffeine\n##### (a) FDA review of caffeine as GRAS\n**(1) In general**\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, (in this subsection referred to as the Commissioner ) shall conduct a review of the safety of caffeine and other stimulants, as the Commissioner determines appropriate, in food (including beverages) and dietary supplements.\n**(2) Elements**\nIn conducting the review under paragraph (1), the Commissioner shall consider the following:\n**(A)**\nWhether caffeine should be considered to be generally recognized to be safe, with respect to consumption by healthy populations, under section 201(s) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(s) ).\n**(B)**\nThe safety of added caffeine or other stimulants, or a complex blend containing a combination of caffeine and other stimulants, in food and dietary supplements.\n**(C)**\nThe safety of guarana, taurine, and similar substances in food and dietary supplements with added caffeine.\n**(D)**\nThresholds for the amount of caffeine, or the amount of a complex blend containing a combination of caffeine and other stimulants, that should be generally recognized as safe when included in food or dietary supplements.\n**(E)**\nWhether any regulations relating to caffeine in food and dietary supplements should be issued or updated.\n**(3) Report**\nNot later than 6 months after the date of enactment of this Act, the Commissioner shall submit to Congress and make publicly available a report detailing the results of the review under paragraph (1).\n**(4) Consideration of results**\nFollowing the completion of the review under paragraph (1), the Secretary of Health and Human Services\u2014\n**(A)**\nshall, in considering the results of such review, make a determination regarding whether caffeine is generally recognized to be safe, with respect to consumption by healthy populations, under section 201(s) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(s) ); and\n**(B)**\nmay consider the results of such review in making a determination pursuant to paragraph (q)(5)(H)(ii)(III) or (z)(3) of section 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) (as inserted by subsection (a)(1)(B)(ii), and added by subsection (b), of section 2 of this Act).\n##### (b) NIH review of caffeine in vulnerable populations\n**(1) In general**\nThe Secretary of Health and Human Services, acting through the Director of the National Institutes of Health, (in this subsection referred to as the Director ) shall conduct or support a review of the effect of the consumption of caffeine and other stimulants, as the Director determines appropriate, on the vulnerable populations described in paragraph (2). The Director may enter into a contract with an appropriate entity under which such entity will conduct such review.\n**(2) Vulnerable populations**\nThe vulnerable populations described in this paragraph are the following:\n**(A)**\nChildren and adolescents.\n**(B)**\nIndividuals with underlying heart conditions.\n**(C)**\nPregnant and breast-feeding women.\n**(D)**\nIndividuals with seizure disorders.\n**(E)**\nIndividuals with mental health conditions that may be worsened by stimulants.\n**(F)**\nCaffeine-sensitive individuals.\n**(G)**\nSuch other individuals as the Director determines appropriate.\n**(3) Report**\nNot later than 6 months after the date of enactment of this Act, the Director shall submit to Congress and make publicly available a report detailing the results of the review under paragraph (1).\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated\u2014\n**(1)**\n$1,000,000 for the purpose of carrying out subsection (a); and\n**(2)**\n$1,000,000 for the purpose of carrying out subsection (b).\n#### 4. Public education campaign on caffeine safety\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, in consultation with the Director of the Centers for Disease Control and Prevention, and working with consumer advocacy and patient groups, shall conduct a public education campaign on the safe consumption of caffeine and caffeinated food (including beverages) and dietary supplements. Such campaign shall pay special attention to the following:\n**(1)**\nThe dangers of the overconsumption of caffeine.\n**(2)**\nThe health impacts caffeine can have on certain vulnerable populations, including\u2014\n**(A)**\nchildren and adolescents;\n**(B)**\nindividuals with underlying heart conditions;\n**(C)**\npregnant and breast-feeding women;\n**(D)**\nindividuals with seizure disorders;\n**(E)**\nindividuals with mental health conditions that may be worsened by stimulants; and\n**(F)**\ncaffeine-sensitive individuals.\n**(3)**\nHow caffeine is marketed to children and adolescents.\n**(4)**\nHow guarana, taurine, and similar substances impact safety.\n**(5)**\nHow to safely consume caffeine.\n#### 5. GAO study and report on marketing of caffeinated beverages\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study on the marketing of caffeinated beverages in restaurants, in stores, and online (including on social media and by social media influencers). In conducting such study, the Comptroller General shall focus on\u2014\n**(1)**\nways in which the marketing of caffeinated beverages (including to children and adults) may be misleading; and\n**(2)**\nhow the marketing of such caffeinated beverages is targeted at children and teens.\n##### (b) Report\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report describing the results of the study conducted under subsection (a), including any recommendations for legislative or administrative action to address the misleading marketing of caffeinated beverages or the targeted marketing of such beverages to children and teens.",
      "versionDate": "2025-03-31",
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
        "name": "Health",
        "updateDate": "2025-04-07T12:30:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119hr2511",
          "measure-number": "2511",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-31",
          "originChamber": "HOUSE",
          "update-date": "2026-02-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2511v00",
            "update-date": "2026-02-17"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sarah Katz Caffeine Safety Act</strong></p><p>This bill establishes labeling and disclosure requirements for caffeinated food, beverages, and supplements.</p><p>Specifically, the bill requires foods and dietary supplements that contain more than 10 milligrams of caffeine to be labeled with (1) their total caffeine content, (2) a statement of whether the caffeine is naturally occurring or is an additive, and (3) an advisory statement indicating that the recommended daily limit of caffeine for healthy adults is 400 milligrams.</p><p>Further, in restaurant chains with 20 or more locations, menus must indicate that an item contains high caffeine where the item contains added caffeine and has a total caffeine content of at least 150 milligrams. Restaurants must place the statement \u201chigh caffeine\u201d or a similar indication adjacent to the name of a covered item on the menu. This requirement applies to both standard and temporary menu items.</p><p>For standard menu items, the bill also expands the nutritional information that restaurants must make available to consumers in written form to include the number of milligrams of caffeine in an item.</p><p>The Food and Drug Administration (FDA) must review the safety of caffeine and other stimulants in food, beverages, and dietary supplements and determine whether caffeine should be generally recognized as safe (GRAS) for healthy adults. (Currently, the FDA considers caffeine as GRAS for cola beverages up to a level of 0.02%.)\u00a0</p><p>Finally, the Government Accountability Office must study and report to Congress on the marketing of caffeinated beverages in restaurants, stores, and online.</p>"
        },
        "title": "Sarah Katz Caffeine Safety Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2511.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah Katz Caffeine Safety Act</strong></p><p>This bill establishes labeling and disclosure requirements for caffeinated food, beverages, and supplements.</p><p>Specifically, the bill requires foods and dietary supplements that contain more than 10 milligrams of caffeine to be labeled with (1) their total caffeine content, (2) a statement of whether the caffeine is naturally occurring or is an additive, and (3) an advisory statement indicating that the recommended daily limit of caffeine for healthy adults is 400 milligrams.</p><p>Further, in restaurant chains with 20 or more locations, menus must indicate that an item contains high caffeine where the item contains added caffeine and has a total caffeine content of at least 150 milligrams. Restaurants must place the statement \u201chigh caffeine\u201d or a similar indication adjacent to the name of a covered item on the menu. This requirement applies to both standard and temporary menu items.</p><p>For standard menu items, the bill also expands the nutritional information that restaurants must make available to consumers in written form to include the number of milligrams of caffeine in an item.</p><p>The Food and Drug Administration (FDA) must review the safety of caffeine and other stimulants in food, beverages, and dietary supplements and determine whether caffeine should be generally recognized as safe (GRAS) for healthy adults. (Currently, the FDA considers caffeine as GRAS for cola beverages up to a level of 0.02%.)\u00a0</p><p>Finally, the Government Accountability Office must study and report to Congress on the marketing of caffeinated beverages in restaurants, stores, and online.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2511"
    },
    "title": "Sarah Katz Caffeine Safety Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sarah Katz Caffeine Safety Act</strong></p><p>This bill establishes labeling and disclosure requirements for caffeinated food, beverages, and supplements.</p><p>Specifically, the bill requires foods and dietary supplements that contain more than 10 milligrams of caffeine to be labeled with (1) their total caffeine content, (2) a statement of whether the caffeine is naturally occurring or is an additive, and (3) an advisory statement indicating that the recommended daily limit of caffeine for healthy adults is 400 milligrams.</p><p>Further, in restaurant chains with 20 or more locations, menus must indicate that an item contains high caffeine where the item contains added caffeine and has a total caffeine content of at least 150 milligrams. Restaurants must place the statement \u201chigh caffeine\u201d or a similar indication adjacent to the name of a covered item on the menu. This requirement applies to both standard and temporary menu items.</p><p>For standard menu items, the bill also expands the nutritional information that restaurants must make available to consumers in written form to include the number of milligrams of caffeine in an item.</p><p>The Food and Drug Administration (FDA) must review the safety of caffeine and other stimulants in food, beverages, and dietary supplements and determine whether caffeine should be generally recognized as safe (GRAS) for healthy adults. (Currently, the FDA considers caffeine as GRAS for cola beverages up to a level of 0.02%.)\u00a0</p><p>Finally, the Government Accountability Office must study and report to Congress on the marketing of caffeinated beverages in restaurants, stores, and online.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr2511"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2511ih.xml"
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
      "title": "Sarah Katz Caffeine Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sarah Katz Caffeine Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to establish certain labeling requirements for caffeine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:17Z"
    }
  ]
}
```
