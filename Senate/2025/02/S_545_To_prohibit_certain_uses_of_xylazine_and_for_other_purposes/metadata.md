# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/545
- Title: Combating Illicit Xylazine Act
- Congress: 119
- Bill type: S
- Bill number: 545
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-04-21T17:24:02Z
- Update date including text: 2026-04-21T17:24:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-03-26 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-15 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-04-15 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 372.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-03-26 - Committee: Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-15 - Committee: Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.
- 2026-04-15 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 372.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/545",
    "number": "545",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Combating Illicit Xylazine Act",
    "type": "S",
    "updateDate": "2026-04-21T17:24:02Z",
    "updateDateIncludingText": "2026-04-21T17:24:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 372.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
            "date": "2026-03-26T14:15:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-12T18:51:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-12T18:51:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NH"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "WA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WV"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "VA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ID"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MS"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "AZ"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "PA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WY"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-24",
      "state": "ME"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "WV"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "ID"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "OK"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TX"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s545is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 545\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Ms. Cortez Masto (for herself, Mr. Grassley , Ms. Hassan , Mrs. Gillibrand , Mrs. Hyde-Smith , Ms. Cantwell , Mr. Scott of Florida , Mrs. Shaheen , Ms. Klobuchar , Mrs. Britt , Mrs. Capito , Mr. Young , Mr. Kelly , Mr. Kaine , Mr. Risch , Ms. Rosen , Mr. Blumenthal , Mr. Luj\u00e1n , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo prohibit certain uses of xylazine, and for other purposes.\n#### 1. Short title\nThis title may be cited as the Combating Illicit Xylazine Act .\n#### 2. Definitions\n##### (a) In general\nIn this title, the term xylazine has the meaning given the term in paragraph (60) of section 102 of the Controlled Substances Act, as added by subsection (b) of this section.\n##### (b) Controlled substances act\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended by adding at the end the following:\n(60) The term xylazine means the substance xylazine, including its salts, isomers, and salts of isomers whenever the existence of such salts, isomers, and salts of isomers is possible. .\n#### 3. Adding xylazine to schedule III\nSchedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812 ) is amended by adding at the end the following:\n(f) Unless specifically excepted or unless listed in another schedule, any material, compound, mixture, or preparation which contains any quantity of xylazine. .\n#### 4. Amendments\n##### (a) Amendment\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended by striking paragraph (27) and inserting the following:\n(27) (A) Except as provided in subparagraph (B), the term ultimate user means a person who has lawfully obtained, and who possesses, a controlled substance for the use by the person or for the use of a member of the household of the person or for an animal owned by the person or by a member of the household of the person. (B) (i) In the case of xylazine, other than for a drug product approved under subsection (b) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ), the term ultimate user means a person\u2014 (I) to whom xylazine was dispensed by\u2014 (aa) a veterinarian registered under this Act; or (bb) a pharmacy registered under this Act pursuant to a prescription of a veterinarian registered under this Act; and (II) who possesses xylazine for\u2014 (aa) an animal owned by the person or by a member of the household of the person; (bb) an animal under the care of the person; (cc) use in government animal-control programs authorized under applicable Federal, State, Tribal, or local law; or (dd) use in wildlife programs authorized under applicable Federal, State, Tribal, or local law. (ii) In this subparagraph, the term person includes\u2014 (I) a government agency or business where animals are located; and (II) an employee or agent of an agency or business acting within the scope of their employment or agency. .\n##### (b) Facilities\nAn entity that manufactures xylazine, as of the date of enactment of this Act, shall not be required to make capital expenditures necessary to install the security standard required of schedule III of the Controlled Substances Act ( 21 U.S.C. 801 et seq. ) for the purposes of manufacturing xylazine.\n##### (c) Labeling\nThe requirements related to labeling, packaging, and distribution logistics of a controlled substance in schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) shall not take effect for xylazine until the date that is 1 year after the date of enactment of this Act.\n##### (d) Practitioner registration\nThe requirements related to practitioner registration, inventory, and recordkeeping of a controlled substance in schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) shall not take effect for xylazine until the date that is 60 days after the date of enactment of this Act. A practitioner that has applied for registration during the 60-day period beginning on the date of enactment of this Act may continue their lawful activities until such application is approved or denied.\n##### (e) Manufacturer transition\nThe Food and Drug Administration and the Drug Enforcement Administration shall facilitate and expedite the relevant manufacturer submissions or applications required by the placement of xylazine on schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ).\n##### (f) Clarification\nNothing in this title, or the amendments made by this title, shall be construed to require the registration of an ultimate user of xylazine under the Controlled Substances Act ( 21 U.S.C. 801 et seq. ) in order to possess xylazine in accordance with subparagraph (B) of section 102(27) of that Act ( 21 U.S.C. 802(27) ), as added by subsection (a) of this section.\n#### 5. Arcos tracking\nSection 307(i) of the Controlled Substances Act ( 21 U.S.C. 827(i) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1)\u2014\n**(A)**\nby inserting or xylazine after gamma hydroxybutyric acid ;\n**(B)**\nby inserting or 512 after section 505 ; and\n**(C)**\nby inserting respectively, after the Federal Food, Drug, and Cosmetic Act, ; and\n**(2)**\nin paragraph (6), by inserting or xylazine after gamma hydroxybutyric acid .\n#### 6. Sentencing Commission\nPursuant to its authority under section 994(p) of title 28, United States Code, the United States Sentencing Commission shall review and, if appropriate, amend its sentencing guidelines, policy statements, and official commentary applicable to persons convicted of an offense under section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ) or section 1010 of the Controlled Substances Import and Export Act ( 21 U.S.C. 960 ) to provide appropriate penalties for offenses involving xylazine that are consistent with the amendments made by this title. In carrying out this section, the Commission should consider the common forms of xylazine as well as its use alongside other scheduled substances.\n#### 7. Report to Congress on xylazine\n##### (a) Initial report\nNot later than 18 months after the date of the enactment of this Act, the Attorney General, acting through the Administrator of the Drug Enforcement Administration and in coordination with the Commissioner of Food and Drugs, shall submit to Congress a report on the prevalence of illicit use of xylazine in the United States and the impacts of such use, including\u2014\n**(1)**\nwhere the drug is being diverted;\n**(2)**\nwhere the drug is originating; and\n**(3)**\nwhether any analogues to xylazine, or related or derivative substances, exist and present a substantial risk of abuse.\n##### (b) Additional report\nNot later than 4 years after the date of the enactment of this Act, the Attorney General, acting through the Administrator of the Drug Enforcement Administration and in coordination with the Commissioner of Food and Drugs, shall submit to Congress a report updating Congress on the prevalence and proliferation of xylazine trafficking and misuse in the United States.",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s545rs.xml",
      "text": "II\nCalendar No. 372\n119th CONGRESS\n2d Session\nS. 545\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Ms. Cortez Masto (for herself, Mr. Grassley , Ms. Hassan , Mrs. Gillibrand , Mrs. Hyde-Smith , Ms. Cantwell , Mr. Scott of Florida , Mrs. Shaheen , Ms. Klobuchar , Mrs. Britt , Mrs. Capito , Mr. Young , Mr. Kelly , Mr. Kaine , Mr. Risch , Ms. Rosen , Mr. Blumenthal , Mr. Luj\u00e1n , Mr. Wicker , Mr. Gallego , Mr. Tillis , Mr. Fetterman , Mr. Bennet , Ms. Lummis , Mr. Budd , Mr. King , Mr. Justice , Mr. Crapo , Mr. McCormick , Mr. Lankford , Mrs. Moody , Mrs. Blackburn , Mr. Cornyn , Mr. Durbin , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nApril 15 (legislative day, April 14), 2026 Reported by Mr. Grassley , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo prohibit certain uses of xylazine, and for other purposes.\n#### 1. Short title\nThis title may be cited as the Combating Illicit Xylazine Act .\n#### 2. Definitions\n##### (a) In general\nIn this title, the term xylazine has the meaning given the term in paragraph (60) of section 102 of the Controlled Substances Act, as added by subsection (b) of this section.\n##### (b) Controlled substances act\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended by adding at the end the following:\n(60) The term xylazine means the substance xylazine, including its salts, isomers, and salts of isomers whenever the existence of such salts, isomers, and salts of isomers is possible. .\n#### 3. Adding xylazine to schedule III\nSchedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812 ) is amended by adding at the end the following:\n(f) Unless specifically excepted or unless listed in another schedule, any material, compound, mixture, or preparation which contains any quantity of xylazine. .\n#### 4. Amendments\n##### (a) Amendment\nSection 102 of the Controlled Substances Act ( 21 U.S.C. 802 ) is amended by striking paragraph (27) and inserting the following:\n(27) (A) Except as provided in subparagraph (B), the term ultimate user means a person who has lawfully obtained, and who possesses, a controlled substance for the use by the person or for the use of a member of the household of the person or for an animal owned by the person or by a member of the household of the person. (B) (i) In the case of xylazine, other than for a drug product approved under subsection (b) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ), the term ultimate user means a person\u2014 (I) to whom xylazine was dispensed by\u2014 (aa) a veterinarian registered under this Act; or (bb) a pharmacy registered under this Act pursuant to a prescription of a veterinarian registered under this Act; and (II) who possesses xylazine for\u2014 (aa) an animal owned by the person or by a member of the household of the person; (bb) an animal under the care of the person; (cc) use in government animal-control programs authorized under applicable Federal, State, Tribal, or local law; or (dd) use in wildlife programs authorized under applicable Federal, State, Tribal, or local law. (ii) In this subparagraph, the term person includes\u2014 (I) a government agency or business where animals are located; and (II) an employee or agent of an agency or business acting within the scope of their employment or agency. .\n##### (b) Facilities\nAn entity that manufactures xylazine, as of the date of enactment of this Act, shall not be required to make capital expenditures necessary to install the security standard required of schedule III of the Controlled Substances Act ( 21 U.S.C. 801 et seq. ) for the purposes of manufacturing xylazine.\n##### (c) Labeling\nThe requirements related to labeling, packaging, and distribution logistics of a controlled substance in schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) shall not take effect for xylazine until the date that is 1 year after the date of enactment of this Act.\n##### (d) Practitioner registration\nThe requirements related to practitioner registration, inventory, and recordkeeping of a controlled substance in schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) shall not take effect for xylazine until the date that is 60 days after the date of enactment of this Act. A practitioner that has applied for registration during the 60-day period beginning on the date of enactment of this Act may continue their lawful activities until such application is approved or denied.\n##### (e) Manufacturer transition\nThe Food and Drug Administration and the Drug Enforcement Administration shall facilitate and expedite the relevant manufacturer submissions or applications required by the placement of xylazine on schedule III of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ).\n##### (f) Clarification\nNothing in this title, or the amendments made by this title, shall be construed to require the registration of an ultimate user of xylazine under the Controlled Substances Act ( 21 U.S.C. 801 et seq. ) in order to possess xylazine in accordance with subparagraph (B) of section 102(27) of that Act ( 21 U.S.C. 802(27) ), as added by subsection (a) of this section.\n#### 5. Arcos tracking\nSection 307(i) of the Controlled Substances Act ( 21 U.S.C. 827(i) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1)\u2014\n**(A)**\nby inserting or xylazine after gamma hydroxybutyric acid ;\n**(B)**\nby inserting or 512 after section 505 ; and\n**(C)**\nby inserting respectively, after the Federal Food, Drug, and Cosmetic Act, ; and\n**(2)**\nin paragraph (6), by inserting or xylazine after gamma hydroxybutyric acid .\n#### 6. Sentencing Commission\nPursuant to its authority under section 994(p) of title 28, United States Code, the United States Sentencing Commission shall review and, if appropriate, amend its sentencing guidelines, policy statements, and official commentary applicable to persons convicted of an offense under section 401 of the Controlled Substances Act ( 21 U.S.C. 841 ) or section 1010 of the Controlled Substances Import and Export Act ( 21 U.S.C. 960 ) to provide appropriate penalties for offenses involving xylazine that are consistent with the amendments made by this title. In carrying out this section, the Commission should consider the common forms of xylazine as well as its use alongside other scheduled substances.\n#### 7. Report to Congress on xylazine\n##### (a) Initial report\nNot later than 18 months after the date of the enactment of this Act, the Attorney General, acting through the Administrator of the Drug Enforcement Administration and in coordination with the Commissioner of Food and Drugs, shall submit to Congress a report on the prevalence of illicit use of xylazine in the United States and the impacts of such use, including\u2014\n**(1)**\nwhere the drug is being diverted;\n**(2)**\nwhere the drug is originating; and\n**(3)**\nwhether any analogues to xylazine, or related or derivative substances, exist and present a substantial risk of abuse.\n##### (b) Additional report\nNot later than 4 years after the date of the enactment of this Act, the Attorney General, acting through the Administrator of the Drug Enforcement Administration and in coordination with the Commissioner of Food and Drugs, shall submit to Congress a report updating Congress on the prevalence and proliferation of xylazine trafficking and misuse in the United States.",
      "versionDate": "2026-04-15",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-02-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1266",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Combating Illicit Xylazine Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "U.S. Sentencing Commission",
            "updateDate": "2025-06-09T18:00:09Z"
          },
          {
            "name": "Veterinary medicine and animal diseases",
            "updateDate": "2025-06-09T18:00:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-21T13:04:04Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s545is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s545rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Combating Illicit Xylazine Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "title": "Combating Illicit Xylazine Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combating Illicit Xylazine Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain uses of xylazine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:30Z"
    }
  ]
}
```
