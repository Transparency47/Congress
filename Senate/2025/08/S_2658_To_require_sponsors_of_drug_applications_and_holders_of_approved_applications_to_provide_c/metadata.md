# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2658?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2658
- Title: Medication Affordability and Patent Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 2658
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2026-03-20T11:03:18Z
- Update date including text: 2026-03-20T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2658",
    "number": "2658",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Medication Affordability and Patent Integrity Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:18Z",
    "updateDateIncludingText": "2026-03-20T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
        "item": [
          {
            "date": "2026-03-19T14:00:42Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-08-01T20:53:11Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2658is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2658\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Ms. Hassan (for herself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require sponsors of drug applications and holders of approved applications to provide certain submissions and communications to the Food and Drug Administration and the United States Patent and Trademark Office.\n#### 1. Short title\nThis Act may be cited as the Medication Affordability and Patent Integrity Act .\n#### 2. Disclosure of information\n##### (a) In general\n**(1) In general**\nSection 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ) is amended by adding at the end the following:\n(7) (A) With respect to any application submitted under this subsection or approved under subsection (c), the sponsor of the application or holder of the approved application shall, for any applicable patent\u2014 (i) certify to the Food and Drug Administration that the information described in subparagraph (B) that is submitted to the Secretary is, to the best knowledge of the sponsor or holder, consistent with the information such sponsor or holder provided to the United States Patent and Trademark Office and any communications such sponsor or holder had with the United States Patent and Trademark Office; and (ii) (I) submit to the United States Patent and Trademark Office any information material to patentability with respect to such applicable patent that the sponsor or holder submits to the Food and Drug Administration, and any information the Food and Drug Administration provided in response; and (II) certify to the United States Patent and Trademark Office that the submission under subclause (I), to the best knowledge of the sponsor or holder, includes all information material to patentability, and is consistent with the information such sponsor or holder provided to the Food and Drug Administration and any communications such sponsor or holder had with the Food and Drug Administration. (B) The information described in this subparagraph is limited to information that is material to patentability, as defined in regulations promulgated by the United States Patent and Trademark Office, and that is\u2014 (i) any statement or characterization of analytical data set forth in the chemistry, manufacturing, and controls section of a new drug application disclosed by the sponsor of the application or holder of the approved application under this section to the United States Patent and Trademark Office that has been, or will be, submitted to the Food and Drug Administration to support the approval of an application under this section; (ii) any statement or characterization with respect to an applicable patent, including any statement or characterization of prior art, submitted by the sponsor of the application or holder of the approved application to the United States Patent and Trademark Office in support of patentability; or (iii) other information, as the Secretary or the Secretary of Commerce may by regulation require. (C) In this paragraph, the term applicable patent means\u2014 (i) a patent that\u2014 (I) claims a drug that is the subject of an application described in subparagraph (A), including any patent that claims, with respect to such a drug, a formulation or composition, method of use, or method of manufacturing; and (II) is issued, assigned, or licensed to the sponsor of the application or holder of the approved application described in subparagraph (A); (ii) an application for a patent described in clause (i)(I) that is sought by the sponsor of the application or holder of the approved application described in subparagraph (A); or (iii) such other patent or application for a patent as the Secretary or the Secretary of Commerce may by regulation require. (D) (i) Except as provided in clause (ii), subparagraph (A) shall apply with respect to any original application submitted under this subsection on or after the date of enactment of the Medication Affordability and Patent Integrity Act and to any amendments or supplements to such original application. (ii) In the case of an application submitted before the date of enactment of the Medication Affordability and Patent Integrity Act , the requirements of subparagraph (A) apply only with respect to\u2014 (I) any applicable patent issued on or after such date of enactment; and (II) in the case of an applicable patent issued before such date of enactment, only to submissions and communications described in clauses (i) and (ii) of subparagraph (A) made on or after such date of enactment. (E) The United States Patent and Trademark Office shall, as necessary, update its applicable regulations or establish new procedures to ensure that any information that the sponsor or holder of the application has submitted to or received from the Food and Drug Administration and that is submitted to the United States Patent and Trademark Office to fulfill the requirements of subparagraph (A), and that would not otherwise be submitted to the United States Patent and Trademark Office, shall remain subject to application protections for trade secret or confidential information or financial information as if the information were held by the Food and Drug Administration. .\n**(2) Inclusion of certifications in application**\nSection 505(b)(1)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b)(1)(A) ) is amended\u2014\n**(A)**\nin clause (vii), by striking and at the end;\n**(B)**\nin clause (viii)(II), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(ix) with respect to each patent listed in the application pursuant to clause (viii) that is an applicable patent (as defined in paragraph (7)(C)), the certifications required under clauses (i) and (ii)(II) of paragraph (7)(A). .\n##### (b) Biological product applications\nSection 351(a)(2) of the Public Health Service Act ( 42 U.S.C. 262(a)(2) ) is amended by adding at the end the following:\n(F) (i) With respect to any application submitted under this subsection or biological product licensed under this subsection, the sponsor of the application or holder of the licensure shall, for any applicable patent\u2014 (I) certify to the Food and Drug Administration that the information described in clause (ii) that is submitted to the Secretary is, to the best knowledge of the sponsor or holder, consistent with the information such sponsor or holder provided to the United States Patent and Trademark Office and any communications such sponsor or holder had with the United States Patent and Trademark Office; and (II) (aa) submit to the United States Patent and Trademark Office any information material to patentability with respect to such applicable patent that the sponsor or holder submits to the Food and Drug Administration provided in response; and (bb) certify to the United States Patent and Trademark Office that the submission under item (aa), to the best knowledge of the sponsor or holder, includes all information material to patentability and is consistent with the information such sponsor or holder provided to the Food and Drug Administration and any communications such sponsor or holder had with the Food and Drug Administration. (ii) The information described in this clause is limited to information that is material to patentability, as defined in regulations promulgated by the United States Patent and Trademark Office, and that is\u2014 (I) any statement or characterization of analytical data set forth in the chemistry, manufacturing, and controls section in a biological product license application disclosed by the sponsor of the application or holder of the approved application under this section to the United States Patent and Trademark Office that has been, or will be, submitted to the Food and Drug Administration to support the approval of an application under this section; (II) any statement or characterization with respect to an applicable patent, including any statement or characterization of prior art, submitted by the sponsor of the application or holder of the approved application to the United States Patent and Trademark Office in support of patentability; or (III) other information, as the Secretary or the Secretary of Commerce may by regulation require. (iii) In this subparagraph, the term applicable patent means\u2014 (I) a patent that\u2014 (aa) claims a biological product that is the subject of an application described in clause (i), including any patent that claims, with respect to such biological product, a formulation or composition, method of use, or method of manufacturing; and (bb) is issued, assigned, or exclusively licensed to the sponsor of the application or holder of the licensure described in clause (i); (II) an application for a patent described in subclause (I)(aa) that is sought by the sponsor of the application or holder of the licensure described in clause (i); or (III) such other patent or application for a patent as the Secretary or Secretary of Commerce may by regulation require. (iv) (I) Except as provided in subclause (II), clause (i) shall apply with respect to any original application submitted under this subsection on or after the date of enactment of the Medication Affordability and Patent Integrity Act and to any amendments or supplements to such original application. (II) In the case of an application submitted under this subsection before the date of enactment of the Medication Affordability and Patent Integrity Act , the requirements of clause (i) apply only with respect to\u2014 (aa) any applicable patent issued on or after such date of enactment; and (bb) in the case of an applicable patent issued before such date of enactment, only to submissions and communications described in subclauses (I) and (II) of clause (i) made on or after such date of enactment. (v) (I) Any information that the sponsor of the application or holder of the licensure has submitted to or received from the Food and Drug Administration that is submitted to the United States Patent and Trademark office to fulfill the requirements of clause (i) shall remain subject to application protections for trade secret or confidential information or financial information as if the information were held by the Food and Drug Administration. (II) The United States Patent and Trademark Office shall, as necessary, update its applicable regulations or create new procedures to ensure compliance with subclause (I) for information submitted under this subparagraph. .\n##### (c) Enforcement\n**(1) FDA enforcement**\nSection 301(q)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(q)(1) ) is amended\u2014\n**(A)**\nin clause (B), by striking ; or and inserting a semicolon;\n**(B)**\nin clause (C), by striking the period and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(D) to submit the certification required under section 505(b)(7) of this Act or section 351(a)(2)(F) of the Public Health Service Act. .\n**(2) Defense against patent infringement actions**\n**(A) In general**\nChapter 28 of title 35, United States Code, is amended by adding at the end the following:\n274. Non-disclosure defense to infringement of drug patent A person shall be entitled to a defense under section 282(b) in an action asserting infringement of an applicable patent (as defined in paragraph (7)(C) of section 505(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(b) ) or subparagraph (F)(ii) of section 351(a)(2) of the Public Health Service Act ( 42 U.S.C. 262(a)(2) )) if the owner or predecessor owner of the applicable patent violated paragraph (7)(A) of such section 505(b) or subparagraph (F)(i) of such section 351(a)(2) with respect to the applicable patent by negligently or intentionally failing to disclose any information required to be disclosed pursuant to such paragraph (7)(A) or such subparagraph (F)(i). .\n**(B) Technical and conforming amendment**\nThe table of sections for chapter 28 of title 35, United States Code, is amended by adding at the end the following:\n274. Non-disclosure defense to infringement of drug patent. .",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T20:11:25Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2658is.xml"
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
      "title": "Medication Affordability and Patent Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medication Affordability and Patent Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require sponsors of drug applications and holders of approved applications to provide certain submissions and communications to the Food and Drug Administration and the United States Patent and Trademark Office.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:20Z"
    }
  ]
}
```
