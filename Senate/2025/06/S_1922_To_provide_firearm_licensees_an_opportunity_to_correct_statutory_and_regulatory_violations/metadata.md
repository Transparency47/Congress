# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1922
- Title: FIREARM Act
- Congress: 119
- Bill type: S
- Bill number: 1922
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2025-12-05T22:49:09Z
- Update date including text: 2025-12-05T22:49:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1922",
    "number": "1922",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "FIREARM Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:09Z",
    "updateDateIncludingText": "2025-12-05T22:49:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-02",
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
          "date": "2025-06-02T19:49:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1922is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1922\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide firearm licensees an opportunity to correct statutory and regulatory violations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act or the FIREARM Act .\n#### 2. Firearm licensing revocations and denials\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) The term self-reported violation means a violation by a licensee of any provision of this chapter or any implementing regulation thereof that the licensee reports to the Attorney General before the Attorney General discovers the violation during an inspection of the licensee under this chapter. (40) The term willfully has the meaning given the term in section 5336(h) of title 31, except that\u2014 (A) the term only includes conduct resulting from or achieved through deliberate planning or specific intent; (B) willfulness shall not be inferred from previous conduct; and (C) minor, clerical, or curable conduct is presumptively not willful. (41) The term uncorrectable violation means any violation that, despite best efforts, cannot be corrected by the licensee, including a violation in which the licensee transferred a firearm to a prohibited person. .\n##### (b) Self-Reported violations; opportunity To correct violations\nSection 923(e) of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting (1) after (e) ; and\n**(2)**\nby adding at the end the following:\n(2) (A) The Attorney General may not bring an enforcement action to revoke, or deny a renewal of, a license for a violation of any provision of this chapter or any implementing regulation thereof on the basis of a self-reported violation, except in the case of a violation\u2014 (i) that is not correctable after the violation occurred; or (ii) in which a firearm was transferred to a person who is prohibited from possessing a firearm pursuant to any provision of this chapter or any implementing regulation thereof. (B) In the case of a self-reported violation, the Attorney General shall\u2014 (i) assist the licensee to correct the self-reported violation; and (ii) provide the licensee with instructions and compliance training designed to assist the licensee in avoiding repetition of the self-reported violation in the future. (3) (A) Before initiating an enforcement action under this subsection, the Attorney General shall provide the licensee with actual notice of the violation giving rise to the enforcement action, which shall include, at a minimum\u2014 (i) a detailed explanation of the substance of the violation; (ii) all evidence or documentation in the possession of the Attorney General regarding the enforcement action; and (iii) a statement that the Attorney General will not initiate the enforcement action if the licensee corrects the violation by the date that is 30 business days after the date on which the licensee first receives actual notice of the violation. (B) The Attorney General may bring an enforcement action under this subsection against a licensee described in subparagraph (A) if\u2014 (i) 30 business days have elapsed since the date on which the licensee received the notice of the violation required under that subparagraph; and (ii) the licensee has not corrected the violation. (C) If a self-reported violation is of a nature such that it cannot be corrected within the grace period and with the assistance provided pursuant to paragraph (2) or (3), the Attorney General may deny a licensee the opportunity to correct. (4) The Attorney General may not bring an enforcement action on the basis of any violation of any provision of this chapter or any implementing regulation thereof that has been corrected pursuant to paragraph (2) or (3) unless the violation involves a prohibited transfer of a firearm or another uncorrectable violation that creates a direct and acute risk of death or serious bodily injury as a result of the uncorrectable violation. .\n##### (c) Direct judicial review of license revocations\nSection 923(f) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking If and inserting Except as provided in paragraph (3), if ; and\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) (A) If after a hearing held under paragraph (2) the Attorney General decides not to reverse his or her decision to deny an application or revoke a license, during the 15-business-day period beginning on the date on which a license holder or applicant receives a written notice of revocation or denial, that aggrieved party may file a petition with the United States district court for the district in which the aggrieved party resides or has his or her principal place of business for a judicial review of the revocation or denial. (B) If a license holder files a petition with a United States district court under subparagraph (A), the Attorney General shall stay the effective date of the revocation until the court issues a judgment. (C) In a proceeding conducted under this paragraph, the court may consider any evidence submitted by the parties to the proceeding, shall review the Attorney General\u2019s decision de novo, and shall uphold any revocation decision only upon a finding, by a preponderance of the evidence, that the license holder willfully violated the statute under this title or any implementing regulation. (D) If the court decides that the Attorney General did not have a sufficient basis to revoke or deny a license, the court shall order the Attorney General to take such action as may be necessary to comply with the judgment of the court. .\n#### 3. Retroactive application to licenses revoked under enhanced regulatory enforcement policy\n##### (a) Definition\nIn this section, the term Enhanced Regulatory Enforcement Policy means the Enhanced Regulatory Enforcement Policy of the Bureau of Alcohol, Tobacco, Firearms and Explosives announced on June 23, 2021.\n##### (b) Retroactive application\nNotwithstanding any provision of law, the provisions of this Act shall apply retroactively to any licensee whose license was revoked or denied pursuant to the Enhanced Regulatory Enforcement Policy.\n##### (c) Restoration of licenses\nIn the case of any licensee whose license was revoked or denied renewal pursuant to the Enhanced Regulatory Enforcement Policy, or who surrendered the license of such licensee at the request or suggestion of an industry operations investigator of the Bureau of Alcohol, Tobacco, Firearms and Explosives during the course of an inspection with respect to which an Enhanced Regulatory Enforcement Policy-type violation was cited or disclosed to the licensee, the Attorney General shall provide the licensee an opportunity to reapply for a license, and approve such application, provided the licensee\u2014\n**(1)**\nhas not been convicted of a violation that would otherwise prohibit the issuance of a license under section 923(d) of title 18, United States Code; and\n**(2)**\nsubmits evidence to demonstrate compliance with the relevant regulations, including corrective action for previously cited violations.",
      "versionDate": "2025-06-02",
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
        "actionDate": "2025-09-10",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 8."
      },
      "number": "3770",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FIREARM Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-16T14:12:42Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-09-16T14:12:42Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-16T14:12:42Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-09-16T14:12:42Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-16T14:12:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-16T17:29:24Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1922is.xml"
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
      "title": "FIREARM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FIREARM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide firearm licensees an opportunity to correct statutory and regulatory violations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:29Z"
    }
  ]
}
```
