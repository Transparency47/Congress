# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3770
- Title: FIREARM Act
- Congress: 119
- Bill type: HR
- Bill number: 3770
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-12-05T22:48:49Z
- Update date including text: 2025-12-05T22:48:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 8.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 8.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3770",
    "number": "3770",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "FIREARM Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:48:49Z",
    "updateDateIncludingText": "2025-12-05T22:48:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 15 - 8.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
        "item": [
          {
            "date": "2025-09-10T15:39:48Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-05T14:06:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WI"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "GA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "CO"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MT"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "KY"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MS"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "CO"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NE"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AZ"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "LA"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "GA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "GA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "MN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "PA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "CO"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "IN"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3770ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3770\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Issa (for himself, Ms. Tenney , Mr. Weber of Texas , Mr. Van Orden , Mr. Collins , Mr. Hunt , Ms. Boebert , Mr. Downing , Mr. Van Drew , Mr. Guthrie , Mr. DesJarlais , Mr. Bilirakis , Mr. Burchett , Mr. Mills , Mr. Guest , Mr. Sessions , Mr. Kustoff , Mr. Evans of Colorado , Mr. Scott Franklin of Florida , Mrs. Miller of Illinois , Mr. Bacon , Mr. Edwards , Mr. Biggs of Arizona , Ms. Stefanik , Mrs. Harshbarger , Mrs. Hinson , Mrs. Luna , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide firearm licensees an opportunity to correct statutory and regulatory violations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act or the FIREARM Act .\n#### 2. Firearm licensing revocations and denials\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) The term self-reported violation means a violation by a licensee of any provision of this chapter or any implementing regulation thereof that the licensee reports to the Attorney General before the Attorney General discovers the violation during an inspection of the licensee under this chapter. (40) The term willfully has the meaning given the term in section 5336(h) of title 31, except that\u2014 (A) the term only includes conduct resulting from or achieved through deliberate planning or specific intent; (B) willfulness shall not be inferred from previous conduct; and (C) minor, clerical, or curable conduct is presumptively not willful. (41) The term uncorrectable violation means any violation that, despite best efforts, cannot be corrected by the licensee, including a violation in which the licensee transferred a firearm to a prohibited person. .\n##### (b) Self-Reported violations; opportunity To correct violations\nSection 923(e) of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting (1) after (e) ; and\n**(2)**\nby adding at the end the following:\n(2) (A) The Attorney General may not bring an enforcement action to revoke, or deny a renewal of, a license for a violation of any provision of this chapter or any implementing regulation thereof on the basis of a self-reported violation, except in the case of a violation\u2014 (i) that is not correctable after the violation occurred; or (ii) in which a firearm was transferred to a person who is prohibited from possessing a firearm pursuant to any provision of this chapter or any implementing regulation thereof. (B) In the case of a self-reported violation, the Attorney General shall\u2014 (i) assist the licensee to correct the self-reported violation; and (ii) provide the licensee with instructions and compliance training designed to assist the licensee in avoiding repetition of the self-reported violation in the future. (3) (A) Before initiating an enforcement action under this subsection, the Attorney General shall provide the licensee with actual notice of the violation giving rise to the enforcement action, which shall include, at a minimum\u2014 (i) a detailed explanation of the substance of the violation; (ii) all evidence or documentation in the possession of the Attorney General regarding the enforcement action; and (iii) a statement that the Attorney General will not initiate the enforcement action if the licensee corrects the violation by the date that is 30 business days after the date on which the licensee first receives actual notice of the violation. (B) The Attorney General may bring an enforcement action under this subsection against a licensee described in subparagraph (A) if\u2014 (i) 30 business days have elapsed since the date on which the licensee received the notice of the violation required under that subparagraph; and (ii) the licensee has not corrected the violation. (C) If a self-reported violation is of a nature such that it cannot be corrected within the grace period and with the assistance provided pursuant to paragraph (2) or (3), the Attorney General may deny a licensee the opportunity to correct. (4) The Attorney General may not bring an enforcement action on the basis of any violation of any provision of this chapter or any implementing regulation thereof that has been corrected pursuant to paragraph (2) or (3) unless the violation involves a prohibited transfer of a firearm or another uncorrectable violation which creates a direct and acute risk of death or serious bodily injury as a result of the uncorrectable violation. .\n##### (c) Direct judicial review of license revocations\nSection 923(f) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking If and inserting Except as provided in paragraph (3), if ; and\n**(2)**\nby amending paragraph (3) to read as follows:\n(3) (A) If after a hearing held under paragraph (2) the Attorney General decides not to reverse his or her decision to deny an application or revoke a license, during the 15-business-day period beginning on the date on which a license holder or applicant receives a written notice of revocation or denial, that aggrieved party may file a petition with the United States district court for the district in which the aggrieved party resides or has his or her principal place of business for a judicial review of the revocation or denial. (B) If a license holder files a petition with a United States district court under subparagraph (A), the Attorney General shall stay the effective date of the revocation until the court issues a judgment. (C) In a proceeding conducted under this paragraph, the court may consider any evidence submitted by the parties to the proceeding, shall review the Attorney General\u2019s decision de novo, and shall uphold any revocation decision only upon a finding, by a preponderance of the evidence, that the license holder willfully violated the statute under this title or any implementing regulation. (D) If the court decides that the Attorney General did not have a sufficient basis to revoke or deny a license, the court shall order the Attorney General to take such action as may be necessary to comply with the judgment of the court. .\n#### 3. Retroactive application to licenses revoked under enhanced regulatory enforcement policy\n##### (a) Retroactive application\nNotwithstanding any provision of law, the provisions of this Act shall apply retroactively to any licensee whose license was revoked or denied pursuant to the Enhanced Regulatory Enforcement Policy announced on June 23, 2021.\n##### (b) Restoration of licenses\nIn the case of any licensee whose license was revoked or denied renewal pursuant to the Enhanced Regulatory Enforcement Policy, or who surrendered their license at the request or suggestion from an ATF Industry Operations Investigator during the course of an inspection with respect to which an Enhanced Regulatory Enforcement Policy type violation was cited or disclosed to the licensee, the Attorney General shall provide the licensee an opportunity to reapply for a license, and approve such application, provided the licensee\u2014\n**(1)**\nhas not been convicted of a violation that would otherwise prohibit the issuance of a license under section 923(d) of title 18, United States Code; and\n**(2)**\nsubmits evidence to demonstrate compliance with the relevant regulations, including corrective action for previously cited violations.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-02",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1922",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FIREARM Act",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-09-16T14:12:18Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-09-16T14:12:28Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-16T14:12:09Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-09-16T14:12:23Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-16T14:12:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-30T13:20:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-05",
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
          "measure-id": "id119hr3770",
          "measure-number": "3770",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-05",
          "originChamber": "HOUSE",
          "update-date": "2025-09-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3770v00",
            "update-date": "2025-09-10"
          },
          "action-date": "2025-06-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act or the FIREARM Act</strong></p><p>This bill prohibits the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) from bringing an enforcement action to revoke or deny renewal of a federal firearms license on the basis of a self-reported violation that is correctable, so long as the violation did not involve the transfer of a firearm to a prohibited person.</p><p>The term <em>self-reported violation</em> means a violation of a statutory provision or implementing regulation by a federal firearms licensee (e.g., a gun dealer) that the licensee reports to the\u00a0ATF before it is discovered during a compliance inspection.</p><p>The bill applies retroactively.</p>"
        },
        "title": "FIREARM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3770.xml",
    "summary": {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act or the FIREARM Act</strong></p><p>This bill prohibits the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) from bringing an enforcement action to revoke or deny renewal of a federal firearms license on the basis of a self-reported violation that is correctable, so long as the violation did not involve the transfer of a firearm to a prohibited person.</p><p>The term <em>self-reported violation</em> means a violation of a statutory provision or implementing regulation by a federal firearms licensee (e.g., a gun dealer) that the licensee reports to the\u00a0ATF before it is discovered during a compliance inspection.</p><p>The bill applies retroactively.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119hr3770"
    },
    "title": "FIREARM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act or the FIREARM Act</strong></p><p>This bill prohibits the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) from bringing an enforcement action to revoke or deny renewal of a federal firearms license on the basis of a self-reported violation that is correctable, so long as the violation did not involve the transfer of a firearm to a prohibited person.</p><p>The term <em>self-reported violation</em> means a violation of a statutory provision or implementing regulation by a federal firearms licensee (e.g., a gun dealer) that the licensee reports to the\u00a0ATF before it is discovered during a compliance inspection.</p><p>The bill applies retroactively.</p>",
      "updateDate": "2025-09-10",
      "versionCode": "id119hr3770"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3770ih.xml"
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
      "title": "FIREARM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIREARM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fighting Irrational Regulatory Enforcement to Avert Retailers\u2019 Misfortune Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide firearm licensees an opportunity to correct statutory and regulatory violations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:34:12Z"
    }
  ]
}
```
