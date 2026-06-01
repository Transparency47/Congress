# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/863?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/863
- Title: Genomic Data Protection Act
- Congress: 119
- Bill type: S
- Bill number: 863
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2025-05-14T15:23:51Z
- Update date including text: 2025-05-14T15:23:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/863",
    "number": "863",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Genomic Data Protection Act",
    "type": "S",
    "updateDate": "2025-05-14T15:23:51Z",
    "updateDateIncludingText": "2025-05-14T15:23:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T18:11:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s863is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 863\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Cassidy (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo provide consumers with the right to delete their genomic data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Genomic Data Protection Act .\n#### 2. Consumer rights regarding privacy of genomic data\n##### (a) Requirements\n**(1) Consumer controls**\n**(A) In general**\nA direct-to-consumer genomic testing company shall provide a simple and effective mechanism to allow a consumer to\u2014\n**(i)**\naccess the genomic data of the consumer; and\n**(ii)**\nsubject to paragraph (4)\u2014\n**(I)**\ndelete the account of the consumer, including any genomic data associated with such account; and\n**(II)**\nrequest the destruction of any biological sample of the consumer.\n**(B) Required mechanism**\nThe direct-to-consumer genomic testing company shall make available to a consumer the mechanism described in subparagraph (A) through the primary means by which the company communicates with the consumer.\n**(2) Notification**\n**(A) Consumer controls and use of deidentified genomic data**\nA direct-to-consumer genomic testing company shall make available, in a clear and conspicuous, not misleading, and easy-to-read manner a notice that\u2014\n**(i)**\nprovides a detailed and accurate representation of the rights set forth in clauses (i) and (ii) of paragraph (1)(A); and\n**(ii)**\ndiscloses that the deidentified genomic data of a consumer may be shared or disclosed to conduct medical or scientific research, consistent with the privacy regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note).\n**(B) Purchase of company**\nIn the event that a direct-to-consumer genomic testing company is purchased or otherwise acquired by another entity, the direct-to-consumer genomic testing company shall send to each consumer, not fewer than 30 days prior to the date on which the purchase or acquisition is complete, a notice that includes\u2014\n**(i)**\nthe identity of the entity purchasing or otherwise acquiring the company; and\n**(ii)**\na detailed and accurate representation of the how a consumer can exercise the rights set forth in clauses (i) and (ii) of paragraph (1)(A) under the new ownership.\n**(3) Processing of deletion or destruction requests**\n**(A) In general**\nWith respect to a consumer's request to delete the genomic data or to destroy the biological sample of the consumer, a direct-to-consumer genomic testing company shall\u2014\n**(i)**\nfulfill such request not later than 30 days after the date on which the consumer makes such request; and\n**(ii)**\nnotify the consumer of such deletion or destruction not later than 30 days after the deletion or destruction.\n**(B) Outstanding requests during purchase of company**\nIn the event that a direct-to-consumer genomic testing company is purchased or otherwise acquired by another entity while a consumer's request to delete the genomic data or to destroy the biological sample of the consumer is outstanding\u2014\n**(i)**\nthe entity that is purchasing or otherwise acquiring the company shall comply with the requirements described in subparagraph (A); and\n**(ii)**\nthe 30-day period to fulfill such request shall begin on the date on which the consumer makes such request to the direct-to-consumer genomic testing company.\n**(4) Exceptions**\nA direct-to-consumer genomic testing company shall not permit a consumer to exercise a right described in paragraph (1)(A)(ii) if the company determines that the exercise of the right would require the deletion of information\u2014\n**(A)**\nsubject to a warrant, lawfully executed subpoena, or other court order; or\n**(B)**\nthe company is required to retain in order to comply with any other applicable legal or regulatory requirement.\n##### (b) Enforcement\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated thereunder shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section or a regulation promulgated thereunder shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Rulemaking**\nNot later than 1 year after the date of enactment of this section, the Commission may promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this section.\n##### (c) Definitions\nIn this section:\n**(1) Biological sample**\nThe term biological sample means any material part of the human, discharge therefrom, or derivative thereof, such as tissue, blood, urine, or saliva, known to contain deoxyribonucleic acid (DNA).\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Consumer**\nThe term consumer means an individual who provides a biological sample to a direct-to-consumer genomic testing company.\n**(4) Deidentified genomic data**\nThe term deidentified genomic data means data that cannot be used to infer information about, or otherwise be linked to, a particular individual, provided that the business that possesses the information does all of the following:\n**(A)**\nTakes reasonable measures to ensure that the information cannot be associated with a particular individual.\n**(B)**\nPublicly commits to maintain and use the information only in deidentified form and not to attempt to reidentify the information, except that the business may attempt to reidentify the information solely for the purpose of determining whether its deidentification processes satisfy the requirements of this subparagraph, provided that the business does not use or disclose any information reidentified in this process and destroys the reidentified information upon completion of that assessment.\n**(C)**\nContractually obligates any recipients of the information to take reasonable measures to ensure that the information cannot be associated with a particular individual and to commit to maintaining and using the information only in deidentified form and not to reidentify the information.\n**(5) Direct-to-consumer genomic testing company**\n**(A) In general**\nThe term direct-to-consumer genomic testing company means a person that does any of the following:\n**(i)**\nManufactures or develops genomic testing products or services for sale directly to consumers.\n**(ii)**\nAnalyzes or interprets genomic data obtained from a consumer.\n**(iii)**\nCollects, uses, maintains, or discloses genomic data collected or derived from a direct-to-consumer genomic testing product or service.\n**(iv)**\nPurchases or acquires genomic data from a direct-to-consumer genomic testing company.\n**(B) Exclusion for health care professionals**\nThe term direct-to-consumer genomic testing company shall not include a health care professional (as defined in section 225 of the Public Health Service Act ( 42 U.S.C. 234 )) that performs an action described in subparagraph (A) for purposes of diagnosis or treatment of a medical condition.\n**(6) Genomic data**\n**(A) In general**\nThe term genomic data \u2014\n**(i)**\nmeans any data, regardless of its format or whether the data has been deidentified, that results from the analysis of a biological sample from a consumer and concerns genomic material; and\n**(ii)**\nincludes\u2014\n**(I)**\ndeoxyribonucleic acids (DNA), ribonucleic acids (RNA), genes, chromosomes, alleles, genomes, alterations or modifications to DNA or RNA, and single nucleotide polymorphisms (SNPs);\n**(II)**\nuninterpreted data that results from the analysis of the biological sample; or\n**(III)**\nany information extrapolated, derived, or inferred therefrom.\n**(B) Exclusion of deidentified genomic data**\nThe term genomic data shall not include the deidentified genomic data of a consumer to the extent that such data is used to conduct medical or scientific research, consistent with the privacy regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note).\n**(7) Genomic testing product or service**\nThe term genomic testing product or service means any testing product or service that analyzes or interprets the genomic data or biological sample of a consumer.\n##### (d) Relationship to Federal and State laws\n**(1) Federal law preservation**\nNothing in this Act, or a regulation promulgated under this Act, shall be construed to limit any other provision of Federal law, except as specifically provided in this Act.\n**(2) State law preservation**\nNothing in this Act, or a regulation promulgated under this Act, shall be construed to preempt, displace, or supplant any State law, except to the extent that a provision of State law conflicts with a provision of this Act, or a regulation promulgated under this Act, and then only to the extent of the conflict.",
      "versionDate": "2025-03-05",
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
        "name": "Commerce",
        "updateDate": "2025-05-14T15:23:51Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s863is.xml"
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
      "title": "Genomic Data Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Genomic Data Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide consumers with the right to delete their genomic data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:28Z"
    }
  ]
}
```
