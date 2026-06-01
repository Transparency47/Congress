# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2008
- Title: Stop Funding Genital Mutilation Act
- Congress: 119
- Bill type: S
- Bill number: 2008
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-07-02T18:11:00Z
- Update date including text: 2025-07-02T18:11:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2008",
    "number": "2008",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Stop Funding Genital Mutilation Act",
    "type": "S",
    "updateDate": "2025-07-02T18:11:00Z",
    "updateDateIncludingText": "2025-07-02T18:11:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T18:26:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2008is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2008\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Cornyn (for himself and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to prohibit Medicaid and CHIP funding for gender transition procedures.\n#### 1. Short title\nThis Act may be cited as the Stop Funding Genital Mutilation Act .\n#### 2. Prohibiting Federal Medicaid and CHIP funding for gender transition procedures\n##### (a) Medicaid\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ;\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amount expended for specified gender transition procedures (as defined in section 1905(kk)) furnished to an individual enrolled in a State plan (or waiver of such plan). ; and\n**(4)**\nin the flush left matter at the end, by striking and (18), and inserting (18), and (28) .\n##### (b) CHIP\nSection 2107(e)(1)(N) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(N) ) is amended by striking and (17) and inserting (17), and (28) .\n##### (c) Specified gender transition procedures defined\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended by adding at the end the following new subsection:\n(kk) Specified gender transition procedures (1) In general For purposes of section 1903(i)(28), except as provided in paragraph (2), the term specified gender transition procedure means, with respect to an individual, any of the following when performed for the purpose of intentionally changing the body of such individual (including by disrupting the body's development, inhibiting its natural functions, or modifying its appearance) to no longer correspond to the individual's sex: (A) Performing any surgery, including\u2014 (i) castration; (ii) sterilization; (iii) orchiectomy; (iv) scrotoplasty; (v) vasectomy; (vi) tubal ligation; (vii) hysterectomy; (viii) oophorectomy; (ix) ovariectomy; (x) metoidioplasty; (xi) clitoroplasty; (xii) reconstruction of the fixed part of the urethra with or without a metoidioplasty or a phalloplasty; (xiii) penectomy; (xiv) phalloplasty; (xv) vaginoplasty; (xvi) vaginectomy; (xvii) vulvoplasty; (xviii) reduction thyrochondroplasty; (xix) chondrolaryngoplasty; (xx) mastectomy; and (xxi) any plastic, cosmetic, or aesthetic surgery that feminizes or masculinizes the facial or other body features of an individual. (B) Any placement of chest implants to create feminine breasts or any placement of erection or testicular prostheses. (C) Any placement of fat or artificial implants in the gluteal region. (D) Administering, prescribing, or dispensing to an individual medications, including\u2014 (i) gonadotropin-releasing hormone (GnRH) analogues or other puberty-blocking drugs to stop or delay normal puberty; and (ii) testosterone, estrogen, or other androgens to an individual at doses that are supraphysiologic than would normally be produced endogenously in a healthy individual of the same age and sex. (2) Exception Paragraph (1) shall not apply to the following when furnished to an individual by a health care provider with the consent of such individual's parent or legal guardian: (A) Puberty suppression or blocking prescription drugs for the purpose of normalizing puberty for an individual experiencing precocious puberty. (B) Medically necessary procedures or treatments to correct for\u2014 (i) a medically verifiable disorder of sex development, including\u2014 (I) 46,XX chromosomes with virilization; (II) 46,XY chromosomes with undervirilization; and (III) both ovarian and testicular tissue; (ii) sex chromosome structure, sex steroid hormone production, or sex hormone action, if determined to be abnormal by a physician through genetic or biochemical testing; (iii) infection, disease, injury, or disorder caused or exacerbated by a previous procedure described in paragraph (1), or a physical disorder, physical injury, or physical illness that would, as certified by a physician, place the individual in imminent danger of death or impairment of a major bodily function unless the procedure is performed, not including procedures performed for the alleviation of mental distress; or (iv) procedures to restore or reconstruct the body of the individual in order to correspond to the individual's sex after one or more previous procedures described in paragraph (1), which may include the removal of a pseudo phallus or breast augmentation. (3) Sex For purposes of paragraph (1), the term sex means either male or female, as biologically determined and defined in paragraphs (4) and (5), respectively. (4) Female For purposes of paragraph (3), the term female means an individual who naturally has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes eggs for fertilization. (5) Male For purposes of paragraph (3), the term male means an individual who naturally has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes sperm for fertilization. .",
      "versionDate": "2025-06-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-01",
        "text": "Message on Senate action sent to the House."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
      "type": "HR"
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
        "updateDate": "2025-07-02T18:11:00Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2008is.xml"
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
      "title": "Stop Funding Genital Mutilation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Funding Genital Mutilation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to prohibit Medicaid and CHIP funding for gender transition procedures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:23Z"
    }
  ]
}
```
