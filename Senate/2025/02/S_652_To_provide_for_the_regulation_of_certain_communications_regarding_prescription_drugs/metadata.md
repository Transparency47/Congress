# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/652
- Title: Protecting Patients from Deceptive Drug Ads Act
- Congress: 119
- Bill type: S
- Bill number: 652
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-01-08T20:08:29Z
- Update date including text: 2026-01-08T20:08:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1129-1130)
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1129-1130)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/652",
    "number": "652",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protecting Patients from Deceptive Drug Ads Act",
    "type": "S",
    "updateDate": "2026-01-08T20:08:29Z",
    "updateDateIncludingText": "2026-01-08T20:08:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1129-1130)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T18:11:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s652is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 652\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Durbin (for himself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for the regulation of certain communications regarding prescription drugs.\n#### 1. Short title\nThis Act may be cited as the Protecting Patients from Deceptive Drug Ads Act .\n#### 2. Regulation of certain communications regarding prescription drugs\n##### (a) Regulation of communications\n**(1) In general**\nSection 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ) is amended by adding at the end the following:\n(h) (1) In the case of a social media influencer or health care provider who makes false or misleading communications regarding a drug approved under section 505 or licensed under section 351 of the Public Health Service Act, and subject to section 503(b), or compounded in accordance with section 503A or 503B, shall be liable to the United States for a civil penalty in an amount described in paragraph (g)(1), in accordance with a process similar to the process described in paragraph (g)(2). (2) For purposes of this paragraph\u2014 (A) the term false or misleading communications \u2014 (i) means advertisements or promotional communications on a social media platform from which there is a financial benefit to the person engaging in such communications regarding such drug\u2014 (I) (aa) that are made knowingly or recklessly; and (bb) contain a false or inaccurate statement or material omission of fact regarding a drug described in subparagraph (1); or (II) fail to include information in brief summary relating to side effects, contraindications, and effectiveness of the drug in the same manner and to the same extent as such information is required in prescription drug advertisements pursuant to section 502(n); and (ii) does not include\u2014 (I) statements that take place in the course of bona fide patient care or medical research that are made by professionals engaged in such patient care or medical research; or (II) statements that describe the person's own experience, opinion, or value judgment; and (B) the term social media influencer means a private individual who has perceived credibility or popularity and who expresses their opinions, beliefs, findings, recommendations, or experience on social media platforms to an audience, including in a manner conveying trust or expertise on a topic, for the purpose to promoting or advertising certain information or products or inducing behavior by the audience. .\n**(2) Guidance**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall issue guidance on how the Secretary will administer paragraph (h) of section 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ), as added by paragraph (1), including with respect to the factors that will be considered in determining whether a communication is false or misleading communication, as defined in such paragraph (h), including\u2014\n**(A)**\nthe various types of statements or omission of facts regarding a prescription drug that would constitute false or misleading, such as statements or omissions related to safety, efficacy, approved or unapproved uses, directions for use from the label approved by the Food and Drug Administration, scientific information, or other similar attributes;\n**(B)**\nwhether the inclusion of the information in brief summary described in paragraph (h)(2)(A)(i)(III) of section 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ), as added by paragraph (1), alone is sufficient in each circumstance to avoid such a determination;\n**(C)**\nactions taken by the social media influencer, health care provider, or other person to demonstrate compliance with such paragraph (h); and\n**(D)**\ncharacteristics specific to various social media platforms, and the speed of dissemination of the content on such platform.\n**(3) Additional requirements for telehealth providers**\n**(A) In general**\nSection 502(n) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(n) ) is amended by adding at the end the following: For purposes of this paragraph, manufacturer, packer, or distributor includes a person who issues or causes to be issued an advertisement or other descriptive printed matter with respect to a specific drug subject to section 503(b)(1) or compounded in accordance with section 503A or 503B, and who directly or indirectly offers to bring together a potential patient and a prescriber or dispenser through use of electronic information and telecommunication technologies to engage in prescribing or dispensing of any drug subject to section 503(b)(1). Nothing in this paragraph shall apply to a private communication between a practitioner licensed by law to prescribe or dispense a prescription drug (or an individual under the direct supervision of such a practitioner) and an individual patient or their representative. .\n**(B) Regulations**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall update the regulations promulgated to carry out section 502(n) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(n) ) in accordance with the amendments made by subparagraph (A).\n**(4) Rule of construction**\nNothing in this subsection, including the amendments made by this subsection, precludes a drug manufacturer from taking any corrective action to mitigate the potential for patient harm from false or misleading communications described in paragraph (h)(2)(A) of section 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353 ), as added by paragraph (1).\n**(5) Effective date**\nThe amendments made by paragraphs (1) and (3) shall take effect 180 days after the date on which the regulations described in paragraph (3)(B) are finalized.\n##### (b) Reporting requirement\n**(1) In general**\nAny payment described in paragraph (2) with respect to the promotion of, or communications regarding, a covered drug shall be treated as a payment from an applicable manufacturer to a covered recipient for purposes of section 1128G of the Social Security Act ( 42 U.S.C. 1320a\u20137h ), and shall be reported to the Secretary of Health and Human Services by the drug manufacturer or health care provider making the payment and made publicly available by the Secretary in accordance with such section 1128G.\n**(2) Payments described**\nA payment described in this paragraph is\u2014\n**(A)**\na payment by a drug manufacturer to a health care provider, including a telehealth company or other similar entity, or social media influencer; or\n**(B)**\na payment by a health care provider, including a telehealth provider or other similar entity, to a social media influencer.\n**(3) Definitions**\nIn this subsection\u2014\n**(A)**\nthe terms applicable manufacturer and covered recipient have the meanings given such terms in section 1128G(e) of the Social Security Act ( 42 U.S.C. 1320a\u20137h ); and\n**(B)**\nthe term covered drug means any drug, including a biological product (as defined in section 351(i) of the Public Health Service Act ( 42 U.S.C. 262(i) )), for which payment is available under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) or a State plan under title XIX or XXI of such Act ( 42 U.S.C. 1396 et seq. ; 42 U.S.C. 1397aa et seq. ) (or a waiver of such a plan).\n##### (c) Market surveillance of prescription drug advertising or promotion\n**(1) In general**\nThe Secretary may conduct market surveillance activities regarding any promotion of prescription drugs on social media platforms. The activities under this section may include\u2014\n**(A)**\nactivities, carried out directly or by contract, relating to\u2014\n**(i)**\naggregating and analysis of public communications (which may involve the use of artificial intelligence applications), including to establish any relationship between a manufacturer of a prescription drug and individuals engaging in communications about such drug;\n**(ii)**\nanalytical tools to review submissions of promotional communications;\n**(iii)**\nengagement with representatives of social media platforms on strategies and opportunities to address false or misleading promotion of prescription drugs, including through methods of technology or functionality to identify and assess false or misleading communications; and\n**(iv)**\ndeveloping and disseminating public facing communications and educational materials and programs for prescription drug manufacturers, social media platforms, and the public, which may include communications and educational materials and programs regarding the Bad Ad program of the Food and Drug Administration;\n**(B)**\nhiring additional staff for the Office of Prescription Drug Promotion of the Center for Drug Evaluation and Research and the Advertising and Promotional Labeling Branch of the Center for Biologics Evaluation and Research for the review of advertising or promotion of prescription drugs on digital platforms, such as social media, and such other purposes as the Secretary determines appropriate; and\n**(C)**\nestablishing a task force, jointly with the Federal Trade Commission, to coordinate and enhance communication between the Federal Trade Commission and the Food and Drug Administration related to monitoring of, and compliance activities relating to, prescription drug advertising or promotion.\n**(2) Rule of construction**\nNothing in paragraph (1) shall be construed to affect the authority of the Secretary to carry out activities described in such paragraph pursuant to other provisions of law.\n**(3) FDA notice to manufacturers**\nThe Secretary may establish a process for providing information to the holder of an approved application of a prescription drug under section 505 of this Act or section 351 of the Public Health Service Act for the purpose of notifying such holder of instances of communications by health care providers or social media influencers that fail to include information in brief summary relating to side effects, contraindications, and effectiveness of the drug in the same manner and to the same extent as such information is required in prescription drug advertisements pursuant to section 502(n) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(n) ).\n**(4) Reporting**\nThe Secretary shall\u2014\n**(A)**\nnot later than 2 years after the date of enactment of this Act, submit to Congress a report on the activities carried out under this subsection;\n**(B)**\nnot later than 4 years after the date of enactment of this Act, submit to Congress, and make publicly available, a report on the activities carried out under this subsection; and\n**(C)**\nmake publicly available on the website of the Food and Drug Administration notice of all enforcement actions taken under paragraph (h) of section 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ), as added by subsection (a).\n**(5) Authorization of appropriations**\nTo carry out this subsection, there are authorized to be appropriated $15,000,000 for each of fiscal years 2025 through 2029.\n##### (d) Social media influencer\nIn this section, the term social media influencer has the meaning given such term in paragraph (h) of section 303 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 333 ), as added by subsection (a).\n##### (e) Severability\nIf any provision of this Act or of any amendment made by this Act, or the application of such provision or amendment to any person or circumstance, is held to be invalid, the remainder of the provisions of this Act and of the amendments made by this Act and the remainder of the provisions of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ), and the application of any such provision or amendment to other persons not similarly situated or to other circumstances, shall not be affected.",
      "versionDate": "2025-02-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-10T15:43:54Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-07-10T15:43:41Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-10T15:44:18Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-07-10T15:43:59Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-10T15:44:10Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-07-10T15:44:04Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-10T15:43:31Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-10T15:44:14Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-07-10T15:43:36Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-07-10T15:43:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-13T15:21:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s652",
          "measure-number": "652",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2026-01-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s652v00",
            "update-date": "2026-01-08"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Patients from Deceptive Drug Ads Act</strong></p><p>This bill establishes civil penalties for false or misleading communications about prescription drugs by certain entities on social media. It also requires additional disclosures and reporting relating to drug advertisements on social media or via telehealth.</p><p>The bill\u2019s civil penalties apply when social media influencers or health care providers make communications regarding prescription drugs, using social media platforms, from which they financially benefit that (1) are made knowingly or recklessly and are\u00a0false or inaccurate, or (2) fail to include the brief summary information (i.e., side effects, contraindications, effectiveness) required in drug advertisements.\u00a0The Food and Drug Administration (FDA) must issue guidance and publish notice of such enforcement actions. The FDA may notify drug manufacturers when such communications fail to include the brief summary information.</p><p>The bill also requires\u00a0telehealth providers (i.e., entities that use telecommunications to bring together patients and drug prescribers or dispensers) to include the brief summary information in prescription drug advertisements.</p><p>Also, payments from drug manufacturers to health care providers or social media influencers, or from health care providers to influencers, for communications promoting prescription drugs must be reported in accordance with anti-kickback laws for federal health care programs.</p><p>Additionally,\u00a0the FDA may conduct market surveillance regarding prescription drug promotion on social media, including analyzing communications and establishing a task force with the Federal Trade Commission.</p>"
        },
        "title": "Protecting Patients from Deceptive Drug Ads Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s652.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Patients from Deceptive Drug Ads Act</strong></p><p>This bill establishes civil penalties for false or misleading communications about prescription drugs by certain entities on social media. It also requires additional disclosures and reporting relating to drug advertisements on social media or via telehealth.</p><p>The bill\u2019s civil penalties apply when social media influencers or health care providers make communications regarding prescription drugs, using social media platforms, from which they financially benefit that (1) are made knowingly or recklessly and are\u00a0false or inaccurate, or (2) fail to include the brief summary information (i.e., side effects, contraindications, effectiveness) required in drug advertisements.\u00a0The Food and Drug Administration (FDA) must issue guidance and publish notice of such enforcement actions. The FDA may notify drug manufacturers when such communications fail to include the brief summary information.</p><p>The bill also requires\u00a0telehealth providers (i.e., entities that use telecommunications to bring together patients and drug prescribers or dispensers) to include the brief summary information in prescription drug advertisements.</p><p>Also, payments from drug manufacturers to health care providers or social media influencers, or from health care providers to influencers, for communications promoting prescription drugs must be reported in accordance with anti-kickback laws for federal health care programs.</p><p>Additionally,\u00a0the FDA may conduct market surveillance regarding prescription drug promotion on social media, including analyzing communications and establishing a task force with the Federal Trade Commission.</p>",
      "updateDate": "2026-01-08",
      "versionCode": "id119s652"
    },
    "title": "Protecting Patients from Deceptive Drug Ads Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Patients from Deceptive Drug Ads Act</strong></p><p>This bill establishes civil penalties for false or misleading communications about prescription drugs by certain entities on social media. It also requires additional disclosures and reporting relating to drug advertisements on social media or via telehealth.</p><p>The bill\u2019s civil penalties apply when social media influencers or health care providers make communications regarding prescription drugs, using social media platforms, from which they financially benefit that (1) are made knowingly or recklessly and are\u00a0false or inaccurate, or (2) fail to include the brief summary information (i.e., side effects, contraindications, effectiveness) required in drug advertisements.\u00a0The Food and Drug Administration (FDA) must issue guidance and publish notice of such enforcement actions. The FDA may notify drug manufacturers when such communications fail to include the brief summary information.</p><p>The bill also requires\u00a0telehealth providers (i.e., entities that use telecommunications to bring together patients and drug prescribers or dispensers) to include the brief summary information in prescription drug advertisements.</p><p>Also, payments from drug manufacturers to health care providers or social media influencers, or from health care providers to influencers, for communications promoting prescription drugs must be reported in accordance with anti-kickback laws for federal health care programs.</p><p>Additionally,\u00a0the FDA may conduct market surveillance regarding prescription drug promotion on social media, including analyzing communications and establishing a task force with the Federal Trade Commission.</p>",
      "updateDate": "2026-01-08",
      "versionCode": "id119s652"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s652is.xml"
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
      "title": "Protecting Patients from Deceptive Drug Ads Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Patients from Deceptive Drug Ads Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the regulation of certain communications regarding prescription drugs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:36Z"
    }
  ]
}
```
