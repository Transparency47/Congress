# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1652?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1652
- Title: Rectifying UDAAP Act
- Congress: 119
- Bill type: HR
- Bill number: 1652
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-12-16T20:21:49Z
- Update date including text: 2025-12-16T20:21:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1652",
    "number": "1652",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Rectifying UDAAP Act",
    "type": "HR",
    "updateDate": "2025-12-16T20:21:49Z",
    "updateDateIncludingText": "2025-12-16T20:21:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MO"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1652ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1652\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Consumer Financial Protection Act of 2010 to clarify standards for UDAAP enforcement actions brought by the Bureau of Consumer Financial Protection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rectifying Undefined Descriptions of Abusive Acts and Practices Act or the Rectifying UDAAP Act .\n#### 2. Mitigating factors in assessing civil penalties\nSection 1055(c) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5565(c) ) is amended by adding at the end the following:\n(6) Rulemaking The Bureau shall, not later than 180 days after the date of the enactment of this paragraph, issue a rule that establishes policies and procedures relating to the imposition of civil monetary penalties sought under this subsection, including the application of the mitigating factors described in paragraph (3). .\n#### 3. Rulemaking relating to unfair, deceptive or abusive acts or practices\n##### (a) In general\nSection 1031 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5531 ) is amended by striking subsection (b) and inserting the following:\n##### (b) Rulemaking\n(1) In general The Bureau may prescribe rules applicable to a covered person or service provider identifying as unlawful unfair, deceptive, or abusive acts or practices in connection with any transaction with a consumer for a consumer financial product or service, or the offering of a consumer financial product or service. Rules under this section may include requirements for the purpose of preventing such acts or practices. (2) Cost benefit analysis required Any final rule issued by the Bureau relating to abusive, unfair, or deceptive acts or practices shall include a cost-benefit analysis. (3) Definition of abusive act or practice The Bureau shall, not later than 180 days after the date of the enactment of this subsection, issue a rule that defines the term abusive act or practice for the purposes of this section. .\n##### (b) Opportunity for comment\nThe Bureau of Consumer Financial Protection shall, not later than 180 days after the date of the enactment of this subsection, allow the public to submit comments with respect to any confusion about how the Bureau of Consumer Financial Protection uses its authority with respect to unfair, deceptive, or abusive acts or practices.\n#### 4. Authority to declare an act unlawful based on discrimination\nThe Bureau of Consumer Financial Protection may not interpret the authority of the Bureau of Consumer Financial Protection relating to unfair, deceptive, or abusive acts and practices, as such term is used in section 1031 of the Consumer Financial Protection Act of 2010, to include discriminatory practices.\n#### 5. Clarifying the abusive standard for the Bureau of Consumer Financial Protection\nSection 1031 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5531 ) is amended by striking subsection (d) and inserting the following:\n(d) Abusive (1) In general The Bureau shall have no authority to declare an act or practice of a covered person abusive in connection with the provision of a consumer financial product or service, unless the act or practice\u2014 (A) intentionally and materially interferes with the ability of a consumer to understand a term or condition of a consumer financial product or service; or (B) takes unreasonable advantage of\u2014 (i) a lack of understanding by the consumer with respect to the possible impact, material risks, costs, or conditions of the product or service, or the likelihood of the risks, costs, or conditions of the product or service negatively affecting the consumer; and (ii) the reasonable reliance the consumer places on an affirmative action or representation of such covered person to induce such consumer to rely on such action or representation. (2) Abusive actions Conduct of a covered person shall be considered abusive if\u2014 (A) the act or practice causes or is likely to cause substantial injury to consumers which is not reasonably avoidable by consumers, provided, however, that if the act or practice was timely, clearly and conspicuously disclosed to consumers, the injury is presumed to be reasonably avoidable; or (B) such substantial injury is not outweighed by countervailing benefits to consumers or to competition. (e) Good-Faith effort To comply (1) In general The Bureau may not seek monetary relief from a covered person under this section unless the covered person has not established by a preponderance of the evidence that they made a good-faith effort to comply. (2) Authority to seek legal or equitable remedies The limitation described in subparagraph (A) shall not restrict the authority of the Bureau to seek legal or equitable remedies, such as damages and restitution, to redress an identifiable consumer injury caused by the abusive acts or practices of such covered person. .\n#### 6. Notice and opportunity to cure\nSection 1031 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5531 ) is amended by adding at the end the following:\n(g) Notice and opportunity To cure (1) In general If a covered person self-identifies a potential unfair, deceptive, or abusive act or practice carried out by such covered person, the Bureau shall, not later than 90 days after such self-identification, provide a written notice in the form of a potential action and request for response letter or a notice and opportunity to respond and advise letter of the potential unfair, deceptive, or abusive act or practice to such covered person and inform the covered person that such person has 180 days after the date the covered person receives such notice to cure such potential unfair, deceptive, or abusive act before the Bureau may pursue other legal action. (2) Tolling of statute of limitations Any applicable statute of limitations that applies to conduct under which the Bureau has given notice and an opportunity to cure shall not toll until\u2014 (A) the covered person cures the potential abusive, unfair, or deceptive act or practice and notifies the Bureau that such act or practice has been cured; (B) the covered person notifies the Bureau that such covered person will not cure the act or practice; or (C) the 180-day period to cure ends. .\n#### 7. Abusive, unfair, or deceptive acts or practices enforcement actions\n##### (a) In general\nSubtitle E of title X of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5561 et seq. ) is amended by adding at the end the following new section:\n1059. Unfair, Deceptive, or Abusive Acts or Practices Enforcement Actions Enforcement actions brought by the Bureau under section 1031 under this title shall be brought in\u2014 (1) the United States district court located where the covered person has its headquarters location; or (2) the United States District Court for the District of Columbia. .\n##### (b) Actions under section 1031\nSection 1031 of the Consumer Financial Protection Act of 2010 is amended by adding at the end the following:\n(g) Enforcement Actions (1) In general If the Bureau brings an enforcement action under this section, the Bureau shall state with particularity the circumstances that the Bureau alleges constitute violation of this section. (2) Alternative Claims If the Bureau brings an enforcement action under this section\u2014 (A) claiming that an activity is unfair or deceptive, the Bureau may not claim in the alternative that the activity is abusive; and (B) claiming that an activity is abusive, the Bureau may not claim in the alternative that the activity is unfair or deceptive. .\n#### 8. Look-back provisions for the Consumer Financial Protection Bureau\nSubtitle B of title X of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5511 et seq. ) is amended by adding at the end the following new section:\n1029B Examination period limitations (a) In general When enforcing Federal consumer financial laws, the Bureau may not seek a civil money penalty for any violating conduct that occurred prior to the most recent assignment of a consumer compliance rating. (b) Rule of construction This limitation described in subsection (a) may not be construed to restrict the ability of the Bureau to seek other forms of legal or equitable relief available under subparagraphs (A) through (G) of section 1055(a)(2) for any violating conduct that occurred prior to the most recent assignment of a consumer compliance rating. .",
      "versionDate": "2025-02-27",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-07T13:06:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1652",
          "measure-number": "1652",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-12-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1652v00",
            "update-date": "2025-12-16"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rectifying Undefined Descriptions of Abusive Acts and Practices Act or the Rectifying UDAAP Act </strong></p><p>This bill restricts the Consumer Financial Protection Bureau\u2019s (CFPB\u2019s) authority to deem a financial act or practice <em>abusive</em> for purposes of enforcement activities. Currently, the CFPB may take enforcement action against a financial product or service provider in connection with any transaction with a consumer for a consumer financial product or service that is unfair, deceptive, or abusive.</p><p>Specifically, the bill prohibits the\u00a0CFPB from including discrimination as an abusive practice. Further, the bill revises what an abusive practice is, including by additionally requiring the practice to intentionally interfere with the ability of a consumer to understand a term or condition.</p><p>The bill also establishes additional criteria for abusive practices. Particularly, a practice is considered abusive if (1) it causes or is likely to cause substantial injury to consumers that is not reasonably avoidable by consumers, where timely disclosed\u00a0conduct is presumed to be reasonably avoidable; or (2) the substantial injury is not outweighed by countervailing benefits to consumers or to competition.</p><p>The bill also eliminates the\u00a0CFPB\u2019s ability to seek monetary relief for unfair, deceptive, or abusive practices if the provider establishes a good faith effort to comply with requirements.\u00a0</p><p>The bill establishes rulemaking requirements, including requiring a cost-benefit analysis for a rule relating to unfair, deceptive, or abusive practices.</p><p>Finally, the bill establishes the right for providers to cure violations if they self-report and limits the CFPB\u2019s use of alternative claims in court.</p>"
        },
        "title": "Rectifying UDAAP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1652.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rectifying Undefined Descriptions of Abusive Acts and Practices Act or the Rectifying UDAAP Act </strong></p><p>This bill restricts the Consumer Financial Protection Bureau\u2019s (CFPB\u2019s) authority to deem a financial act or practice <em>abusive</em> for purposes of enforcement activities. Currently, the CFPB may take enforcement action against a financial product or service provider in connection with any transaction with a consumer for a consumer financial product or service that is unfair, deceptive, or abusive.</p><p>Specifically, the bill prohibits the\u00a0CFPB from including discrimination as an abusive practice. Further, the bill revises what an abusive practice is, including by additionally requiring the practice to intentionally interfere with the ability of a consumer to understand a term or condition.</p><p>The bill also establishes additional criteria for abusive practices. Particularly, a practice is considered abusive if (1) it causes or is likely to cause substantial injury to consumers that is not reasonably avoidable by consumers, where timely disclosed\u00a0conduct is presumed to be reasonably avoidable; or (2) the substantial injury is not outweighed by countervailing benefits to consumers or to competition.</p><p>The bill also eliminates the\u00a0CFPB\u2019s ability to seek monetary relief for unfair, deceptive, or abusive practices if the provider establishes a good faith effort to comply with requirements.\u00a0</p><p>The bill establishes rulemaking requirements, including requiring a cost-benefit analysis for a rule relating to unfair, deceptive, or abusive practices.</p><p>Finally, the bill establishes the right for providers to cure violations if they self-report and limits the CFPB\u2019s use of alternative claims in court.</p>",
      "updateDate": "2025-12-16",
      "versionCode": "id119hr1652"
    },
    "title": "Rectifying UDAAP Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rectifying Undefined Descriptions of Abusive Acts and Practices Act or the Rectifying UDAAP Act </strong></p><p>This bill restricts the Consumer Financial Protection Bureau\u2019s (CFPB\u2019s) authority to deem a financial act or practice <em>abusive</em> for purposes of enforcement activities. Currently, the CFPB may take enforcement action against a financial product or service provider in connection with any transaction with a consumer for a consumer financial product or service that is unfair, deceptive, or abusive.</p><p>Specifically, the bill prohibits the\u00a0CFPB from including discrimination as an abusive practice. Further, the bill revises what an abusive practice is, including by additionally requiring the practice to intentionally interfere with the ability of a consumer to understand a term or condition.</p><p>The bill also establishes additional criteria for abusive practices. Particularly, a practice is considered abusive if (1) it causes or is likely to cause substantial injury to consumers that is not reasonably avoidable by consumers, where timely disclosed\u00a0conduct is presumed to be reasonably avoidable; or (2) the substantial injury is not outweighed by countervailing benefits to consumers or to competition.</p><p>The bill also eliminates the\u00a0CFPB\u2019s ability to seek monetary relief for unfair, deceptive, or abusive practices if the provider establishes a good faith effort to comply with requirements.\u00a0</p><p>The bill establishes rulemaking requirements, including requiring a cost-benefit analysis for a rule relating to unfair, deceptive, or abusive practices.</p><p>Finally, the bill establishes the right for providers to cure violations if they self-report and limits the CFPB\u2019s use of alternative claims in court.</p>",
      "updateDate": "2025-12-16",
      "versionCode": "id119hr1652"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1652ih.xml"
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
      "title": "Rectifying UDAAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rectifying UDAAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rectifying Undefined Descriptions of Abusive Acts and Practices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consumer Financial Protection Act of 2010 to clarify standards for UDAAP enforcement actions brought by the Bureau of Consumer Financial Protection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:25Z"
    }
  ]
}
```
