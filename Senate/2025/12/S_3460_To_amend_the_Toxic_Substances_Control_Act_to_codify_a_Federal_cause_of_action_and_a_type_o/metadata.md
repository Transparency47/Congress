# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3460
- Title: PFAS Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3460
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-01-07T15:59:49Z
- Update date including text: 2026-01-07T15:59:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3460",
    "number": "3460",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "PFAS Accountability Act of 2025",
    "type": "S",
    "updateDate": "2026-01-07T15:59:49Z",
    "updateDateIncludingText": "2026-01-07T15:59:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T20:18:33Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3460is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3460\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mrs. Gillibrand introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Toxic Substances Control Act to codify a Federal cause of action and a type of remedy available for individuals significantly exposed to per- and polyfluoroalkyl substances, to encourage research and accountability for irresponsible discharge of those substances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PFAS Accountability Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe Centers for Disease Control and Prevention has detected numerous perfluoroalkyl and polyfluoroalkyl substances (referred to in this Act as PFAS ) in the blood serum of individuals in the United States, all of which come from manufacturing and use of PFAS by humans, as there is no natural source of PFAS in human blood;\n**(2)**\npeer-reviewed studies by other organizations have detected PFAS in the drinking water of at least 200,000,000 individuals in the United States;\n**(3)**\nPFAS are introduced into the market every year, and little research is conducted to ensure the safety of PFAS for individuals;\n**(4)**\nas of the day before the date of enactment of this Act, a Federal statutory cause of action does not exist for individuals harmed by the long-term effects of PFAS exposure; and\n**(5)**\nPFAS exposure, even at low levels, has been linked to chronic diseases, including cancer, reproductive and developmental harms, and harms to the immune system.\n#### 3. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto encourage PFAS research and provide accountability for irresponsible PFAS manufacturing and irresponsible use of PFAS in manufacturing by codifying\u2014\n**(A)**\na Federal cause of action for individuals significantly exposed to PFAS; and\n**(B)**\na medical monitoring remedy for those individuals;\n**(2)**\nto help address harm to individuals significantly exposed to PFAS by\u2014\n**(A)**\ncodifying that harm as an injury at law and equity; and\n**(B)**\nshifting the costs of medical monitoring from those individuals to the parties responsible for the exposure; and\n**(3)**\nto provide incentives for industry to fund PFAS safety research.\n#### 4. Cause of action and remedies\n##### (a) In general\nThe Toxic Substances Control Act is amended by inserting after section 24 ( 15 U.S.C. 2623 ) the following:\n25. Individuals exposed to perfluoroalkyl and polyfluoroalkyl substances (a) Definition of PFAS In this section, the term PFAS means a perfluoroalkyl or polyfluoroalkyl substance with at least 1 fully fluorinated carbon atom. (b) Cause of action An individual who is significantly exposed to PFAS or has reasonable grounds to suspect that the individual was significantly exposed to PFAS may bring a claim, individually or on behalf of a class of similarly situated individuals, in any district court of the United States for appropriate legal and equitable relief against any person that\u2014 (1) engaged in any portion of a manufacturing process that created the PFAS to which the individual was significantly exposed, including any telomer, fluorosurfactant, or toll manufacturing process leading to the creation of the PFAS to which the individual was significantly exposed; and (2) foresaw or reasonably should have foreseen that the creation or use of PFAS would result in human exposure to PFAS. (c) Medical monitoring (1) In general A court may award medical monitoring to an individual or class of individuals bringing a claim under subsection (b) if\u2014 (A) the individual or class has been significantly exposed to PFAS; (B) as a result of that exposure, the individual or class has suffered an increased risk of developing a disease associated with exposure to PFAS; (C) as a result of that increased risk, there is a reasonable basis for the individual or class to undergo periodic diagnostic medical examinations of a nature or frequency that is different from or additional to what would be prescribed in the absence of the exposure; and (D) those medical examinations are effective in detecting a disease associated with exposure to PFAS. (2) Presumption of significant exposure (A) Individuals An individual plaintiff shall be presumed to have been significantly exposed to PFAS under paragraph (1)(A) if the individual\u2014 (i) demonstrates that\u2014 (I) the defendant engaged in any portion of a manufacturing process that created the PFAS to which the individual was significantly exposed, including any telomer, fluo\u00adro\u00adsur\u00adfac\u00adtant, or toll manufacturing pro\u00adcess leading to the creation of the PFAS to which the individual was significantly exposed; and (II) the PFAS described in subclause (I) were released into 1 or more areas where the individual would have been exposed for a cumulative period of not less than 1 year; or (ii) offers testing results that demonstrate that PFAS or metabolites of PFAS have been or are currently detected in the body or blood serum of the individual. (B) Class actions In a class action, a presumption of significant exposure to PFAS under paragraph (1)(A) shall be established for the class by\u2014 (i) demonstrating that\u2014 (I) the defendant engaged in any portion of a manufacturing process that created the PFAS to which the class members were significantly exposed, including any telomer, fluo\u00adro\u00adsur\u00adfac\u00adtant, or toll manufacturing pro\u00adcess leading to the creation of the PFAS to which the class members were significantly exposed; and (II) the PFAS described in subclause (I) were released into 1 or more areas where a representative portion of the class members would have been exposed for a cumulative period of not less than 1 year; or (ii) offering testing results that demonstrate that PFAS or metabolites of PFAS have been or are currently detected in the bodies of a representative portion of class members that share sufficient common exposure characteristics with the class. (3) Rebutting the presumption (A) In general A defendant may rebut a presumption of significant exposure with respect to an individual plaintiff or class member for which testing results are not offered under subparagraph (A)(ii) or (B)(ii) of paragraph (2) by offering results for that individual or class member of testing that\u2014 (i) uses a generally accepted method for detecting the particular PFAS or metabolites of PFAS at issue; (ii) is performed by an independent provider agreed on by both parties; and (iii) confirms that the relevant PFAS or metabolites of PFAS likely were not present in the body of the individual or class member at the relevant time in a sufficient quantity to qualify as significant exposure under paragraph (1)(A). (B) Costs A defendant shall be responsible for the costs of testing under subparagraph (A). (C) Independent provider If both parties cannot agree on an independent provider under subparagraph (A)(ii), the court shall appoint an independent provider. (4) Increased risk of developing disease (A) In general If there is insufficient toxicological data to reasonably determine whether an individual or class has suffered an increased risk of developing a disease associated with exposure to any individual PFAS or group of PFAS under paragraph (1)(B), a court may lower the standard for scientific proof with regard to the increased risk of developing that disease until independent and reliable toxicological data is available with respect to that individual PFAS or group of PFAS. (B) Ordering studies To make available independent and reliable toxicological data described in subparagraph (A) with respect to an individual PFAS or group of PFAS, a court may order new or additional epidemiological, toxicological, or other studies or investigations of that individual PFAS or group of PFAS as part of a medical monitoring remedy awarded under paragraph (1). (d) Sense of Congress It is the sense of Congress that courts should encourage more reliable and independent research into the latent health effects of PFAS. (e) Effect on State law claims and remedies Nothing in this section\u2014 (1) preempts, alters, bars, or precludes any State law claims or remedies, including any State law claims or remedies for an injury addressed by this section; or (2) provides an exclusive claim or remedy. .\n##### (b) Clerical amendment\nThe table of contents for the Toxic Substances Control Act ( Public Law 94\u2013469 ; 90 Stat. 2003) is amended by inserting after the item relating to section 24 the following:\nSec. 25. Individuals exposed to perfluoroalkyl and polyfluoroalkyl substances. .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6626",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PFAS Accountability Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2026-01-07T15:59:24Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3460is.xml"
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
      "title": "PFAS Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PFAS Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Toxic Substances Control Act to codify a Federal cause of action and a type of remedy available for individuals significantly exposed to per- and polyfluoroalkyl substances, to encourage research and accountability for irresponsible discharge of those substances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:21Z"
    }
  ]
}
```
