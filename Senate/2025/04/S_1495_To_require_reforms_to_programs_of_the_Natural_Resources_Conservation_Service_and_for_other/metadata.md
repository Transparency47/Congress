# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1495?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1495
- Title: NRCS Wetland Compliance and Appeals Reform Act
- Congress: 119
- Bill type: S
- Bill number: 1495
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-09T15:11:48Z
- Update date including text: 2025-12-09T15:11:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1495",
    "number": "1495",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "NRCS Wetland Compliance and Appeals Reform Act",
    "type": "S",
    "updateDate": "2025-12-09T15:11:48Z",
    "updateDateIncludingText": "2025-12-09T15:11:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-11T02:40:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ND"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1495is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1495\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Rounds (for himself, Mr. Hoeven , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require reforms to programs of the Natural Resources Conservation Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NRCS Wetland Compliance and Appeals Reform Act .\n#### 2. Natural Resources Conservation Service reforms\n##### (a) Permissibility of the removal of woody vegetation\nSection 1221(d) of the Food Security Act of 1985 ( 16 U.S.C. 3821(d) ) is amended by adding at the end the following:\n(3) Permissibility of the removal of woody vegetation The removal of woody vegetation, including stumps, shall not be considered to be an activity that is for the purpose, or that has the effect, of making the production of an agricultural commodity possible under paragraph (1). .\n##### (b) Prohibition on retroactive penalties\nSection 1221 of the Food Security Act of 1985 ( 16 U.S.C. 3821 ) is amended by adding at the end the following:\n(g) Prohibition on retroactive penalties The Secretary may not determine a person to be in violation of this section for the production of an agricultural commodity on, or the conversion of, a wetland that, at the time of that production or conversion, as applicable, the Secretary had not delineated, determined, and certified to be a wetland in accordance with section 1222. .\n##### (c) Burden of proof\nSection 1221 of the Food Security Act of 1985 ( 16 U.S.C. 3821 ) (as amended by subsection (b)) is amended by adding at the end the following:\n(h) Burden of proof The Secretary shall bear the burden of proving, by clear and convincing evidence, that a person is in violation of this section, including\u2014 (1) in a case in which there is a lack of evidence to determine such a violation; and (2) the burden of proving, by clear and convincing evidence, that evidence offered to prove that a person is not in violation of this section is unreliable. .\n##### (d) Prohibition on using new rationale for wetland determinations previously refuted\nSection 1222(a) of the Food Security Act of 1985 ( 16 U.S.C. 3822(a) ) is amended by adding at the end the following:\n(7) Prohibition on using new rationale for wetland determinations previously refuted If a person successfully appeals a final wetland determination at the National Appeals Division, the Secretary may not subsequently make a determination that the wetland exists based on a rationale that was not used for the determination that was successfully appealed at the National Appeals Division. .\n##### (e) Appeal process for nonaccepted review of wetland certification requests\nSection 1222(a) of the Food Security Act of 1985 ( 16 U.S.C. 3822(a) ) (as amended by subsection (d)) is amended by adding at the end the following:\n(8) Appeal process for nonaccepted review of wetland certification requests The Secretary shall develop an appeal process for requests for the review of wetland certifications that are not accepted by a State office of the Natural Resources Conservation Service, which shall include a right for the person bringing the appeal to demand that the Secretary conduct an on-site visit in accordance with subsection (c). .\n##### (f) Requirement relating to preliminary wetland determinations\nSection 1222(c) of the Food Security Act of 1985 ( 16 U.S.C. 3822(c) ) is amended by adding at the end the following:\n(3) Requirement relating to preliminary wetland determinations The Secretary may not rely solely on 1 on-site visit described in paragraph (1) to determine that the hydrologic criteria for the determination that a wetland exists are satisfied. .\n##### (g) Customer satisfaction survey\nSubtitle C of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3821 et seq. ) is amended by adding at the end the following:\n1225. Customer satisfaction survey (a) Purposes The purposes of this section are\u2014 (1) to improve customer service at the Natural Resources Conservation Service relating to the administration of this subtitle; (2) to identify areas of satisfaction of customers in interacting with the Natural Resources Conservation Service in the administration of this subtitle; (3) to identify areas of customer service at the Natural Resources Conservation Service in need of improvement due to dissatisfaction of customers in interacting with the Natural Resources Conservation Service in the administration of this subtitle; and (4) to address corrective measures and initiate positive change in customer service at the Natural Resources Conservation Service relating to the administration of this subtitle. (b) Option To participate in survey The Secretary shall offer to each individual who interacts with the Natural Resources Conservation Service in the administration of this subtitle the option to participate in a survey described in subsection (c). (c) Surveys The Secretary shall enter into an agreement with an independent survey company, under which the independent survey company shall provide the following services: (1) Send, by email or mail, a customer satisfaction survey to each individual who interacts with the Natural Resources Conservation Service in the administration of this subtitle and indicates to the Secretary a desire to participate in the survey on being offered the option to participate under subsection (b) after any of the following occurs: (A) The Secretary completes a final wetland determination, including a final technical determination, relating to land of the individual. (B) Appeals to the Farm Service Agency with respect to a wetland determination are exhausted. (C) An appeal is made with respect to a wetland determination to a National Appeals Division officer. (D) An appeal is made with respect to a wetland determination to the Director of the National Appeals Division. (E) The Secretary completes a review of a prior certification of a wetland determination. (F) The individual has any other interaction with the Natural Resources Conservation Service, as the Secretary determines to be appropriate. (2) Receive responses to the surveys from the individuals to which the surveys are sent under paragraph (1). (3) Each month\u2014 (A) compile the responses to the surveys received under paragraph (2); and (B) submit a report describing the compiled responses to\u2014 (i) the applicable State Conservationist; (ii) the congressional delegation of each applicable State; (iii) the Committee on Agriculture, Nutrition, and Forestry of the Senate; (iv) the Committee on Agriculture of the House of Representatives; (v) the applicable State department of agriculture; and (vi) the Secretary. .\n##### (h) State oversight committees\nSubtitle C of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3821 et seq. ) (as amended by subsection (g)) is amended by adding at the end the following:\n1226. State oversight committees (a) In general The Secretary shall establish an oversight committee for each State in which appeals of wetland determinations under this subtitle are made. (b) Composition Each State oversight committee shall be composed of\u2014 (1) 2 private, active farmers or ranchers appointed by the Secretary; and (2) 1 private, active farmer or rancher appointed by the State department of agriculture. (c) Terms A member of a State oversight committee\u2014 (1) shall be appointed for a term of 5 years; and (2) may serve for not more than 2 terms. (d) Duties Each State oversight committee shall have the following duties: (1) Review the following appeals of wetland determinations under this subtitle in the applicable State: (A) Appeals of preliminary wetland determinations. (B) Appeals of final wetland determinations. (C) Wetland determination appeals to the county Farm Service Agency committee. (D) Wetland determination appeals for State Conservationist review. (E) Requests for wetland determination mediation. (F) Wetland determination appeals to the National Appeals Division. (G) Wetland determination appeals to the Director of the National Appeals Division. (2) Review all requests for a review of a prior certification of a wetland determination under this subtitle. (3) Submit a report describing findings of fact and recommendations for change and improvement with respect to each review under paragraphs (1) and (2) to\u2014 (A) the State Conservationist; (B) the Chief of the Natural Resources Conservation Service; (C) the Committee on Agriculture, Nutrition, and Forestry of the Senate; and (D) the Committee on Agriculture of the House of Representatives. (e) Assistance A State oversight committee may procure assistance in carrying out the duties under subsection (d) from\u2014 (1) a consultant; and (2) a legal services provider. .\n##### (i) Reforms to appeals processes\nThe Secretary of Agriculture shall\u2014\n**(1)**\nrequire National Appeals Division judges and agency heads of the Department of Agriculture to receive retraining on providing a fair and balanced hearing;\n**(2)**\nprovide to a person the entire record or decisional documentation relating to an allegation of the Secretary that the person is in violation of section 1221 of the Food Security Act of 1985 ( 16 U.S.C. 3821 ) at the time the Secretary makes the allegation;\n**(3)**\nallow a person (or counsel of the person) to call technical staff of the Natural Resources Conservation Service as a witness in an appeal brought by the person relating to a delineation, determination, or certification of a wetland under section 1222 of that Act ( 16 U.S.C. 3822 );\n**(4)**\nin an appeal described in paragraph (3), accept evidence provided by the person bringing the appeal as reliable absent substantial evidence that the evidence provided by the person is not reliable; and\n**(5)**\ncompensate a person for fees and expenses, including legal fees, when the person successfully appeals a delineation, determination, or certification described in paragraph (3) and has incurred legal costs as a result of the overturned delineation, determination, or certification, as applicable.\n##### (j) Regulations\nSection 1246(b)(2) of the Food Security Act of 1985 ( 16 U.S.C. 3846(b)(2) ) is amended\u2014\n**(1)**\nby striking (2) shall and inserting the following:\n(2) (A) except as provided in subparagraph (B), shall ;\n**(2)**\nin subparagraph (A) (as so designated), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(B) shall be promulgated in accordance with section 553 of title 5, United States Code, in the case of\u2014 (i) subtitles B and C; (ii) section 1201, to the extent that section defines a term that appears in, or otherwise relates to, subtitle B or C; and (iii) subtitle E, to the extent that subtitle relates to subtitle B or C. .\n##### (k) Prohibition of permanent easements\nNotwithstanding any other provision of law, the Secretary of Agriculture, acting through the Chief of the Natural Resources Conservation Service, may not acquire any permanent easement.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T13:37:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s1495",
          "measure-number": "1495",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-12-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1495v00",
            "update-date": "2025-12-09"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>NRCS Wetland Compliance and Appeals Reform Act </strong></p><p>This bill revises provisions related to compliance and the appeals process for the wetland certification program at the Natural Resources Conservation Service (NRCS).</p><p>Among\u00a0other things, this bill</p><ul><li>prohibits the NRCS from acquiring any permanent easement;</li><li>prohibits the Department of Agriculture (USDA) from imposing penalties retroactively for newly determined wetlands;</li><li>revises the appeals process of the\u00a0NRCS for wetland certification requests;</li><li>prohibits USDA from using new rationale for a wetland determination if a person has previously successfully appealed a final wetland determination;</li><li>establishes that USDA bears the burden of proof, by clear and convincing evidence, that a person has violated certain wetland conservation provisions;</li><li>requires USDA to establish oversight committees in each state that will oversee the appeals of wetland determinations; and</li><li>requires that each individual who interacts with the\u00a0NRCS have the option to participate in a customer satisfaction survey provided by an independent survey company.</li></ul><p>In addition, USDA must modify the appeals process to provide the person appealing with certain USDA records or documentation relating to the compliance violations.</p><p>Further, in an appeal that is related to a delineation, determination, or certification of a wetland, USDA must modify the process to (1) allow a person to call\u00a0NRCS technical staff as a witness, (2) accept evidence provided by the person bringing the appeal as reliable absent substantial evidence that it is not reliable, and (3) compensate a person who successfully appeals for fees and expenses.</p>"
        },
        "title": "NRCS Wetland Compliance and Appeals Reform Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1495.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>NRCS Wetland Compliance and Appeals Reform Act </strong></p><p>This bill revises provisions related to compliance and the appeals process for the wetland certification program at the Natural Resources Conservation Service (NRCS).</p><p>Among\u00a0other things, this bill</p><ul><li>prohibits the NRCS from acquiring any permanent easement;</li><li>prohibits the Department of Agriculture (USDA) from imposing penalties retroactively for newly determined wetlands;</li><li>revises the appeals process of the\u00a0NRCS for wetland certification requests;</li><li>prohibits USDA from using new rationale for a wetland determination if a person has previously successfully appealed a final wetland determination;</li><li>establishes that USDA bears the burden of proof, by clear and convincing evidence, that a person has violated certain wetland conservation provisions;</li><li>requires USDA to establish oversight committees in each state that will oversee the appeals of wetland determinations; and</li><li>requires that each individual who interacts with the\u00a0NRCS have the option to participate in a customer satisfaction survey provided by an independent survey company.</li></ul><p>In addition, USDA must modify the appeals process to provide the person appealing with certain USDA records or documentation relating to the compliance violations.</p><p>Further, in an appeal that is related to a delineation, determination, or certification of a wetland, USDA must modify the process to (1) allow a person to call\u00a0NRCS technical staff as a witness, (2) accept evidence provided by the person bringing the appeal as reliable absent substantial evidence that it is not reliable, and (3) compensate a person who successfully appeals for fees and expenses.</p>",
      "updateDate": "2025-12-09",
      "versionCode": "id119s1495"
    },
    "title": "NRCS Wetland Compliance and Appeals Reform Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>NRCS Wetland Compliance and Appeals Reform Act </strong></p><p>This bill revises provisions related to compliance and the appeals process for the wetland certification program at the Natural Resources Conservation Service (NRCS).</p><p>Among\u00a0other things, this bill</p><ul><li>prohibits the NRCS from acquiring any permanent easement;</li><li>prohibits the Department of Agriculture (USDA) from imposing penalties retroactively for newly determined wetlands;</li><li>revises the appeals process of the\u00a0NRCS for wetland certification requests;</li><li>prohibits USDA from using new rationale for a wetland determination if a person has previously successfully appealed a final wetland determination;</li><li>establishes that USDA bears the burden of proof, by clear and convincing evidence, that a person has violated certain wetland conservation provisions;</li><li>requires USDA to establish oversight committees in each state that will oversee the appeals of wetland determinations; and</li><li>requires that each individual who interacts with the\u00a0NRCS have the option to participate in a customer satisfaction survey provided by an independent survey company.</li></ul><p>In addition, USDA must modify the appeals process to provide the person appealing with certain USDA records or documentation relating to the compliance violations.</p><p>Further, in an appeal that is related to a delineation, determination, or certification of a wetland, USDA must modify the process to (1) allow a person to call\u00a0NRCS technical staff as a witness, (2) accept evidence provided by the person bringing the appeal as reliable absent substantial evidence that it is not reliable, and (3) compensate a person who successfully appeals for fees and expenses.</p>",
      "updateDate": "2025-12-09",
      "versionCode": "id119s1495"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1495is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NRCS Wetland Compliance and Appeals Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NRCS Wetland Compliance and Appeals Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require reforms to programs of the Natural Resources Conservation Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:28Z"
    }
  ]
}
```
