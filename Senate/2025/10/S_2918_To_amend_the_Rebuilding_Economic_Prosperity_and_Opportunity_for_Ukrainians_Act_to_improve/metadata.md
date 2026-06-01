# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2918
- Title: REPO Implementation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2918
- Origin chamber: Senate
- Introduced date: 2025-09-19
- Update date: 2026-04-22T11:03:21Z
- Update date including text: 2026-04-22T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in Senate
- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 243.
- Latest action: 2025-09-19: Introduced in Senate

## Actions

- 2025-09-19 - IntroReferral: Introduced in Senate
- 2025-09-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 243.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2918",
    "number": "2918",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "REPO Implementation Act of 2025",
    "type": "S",
    "updateDate": "2026-04-22T11:03:21Z",
    "updateDateIncludingText": "2026-04-22T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 243.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-19",
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
            "date": "2025-10-30T15:38:23Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:11:44Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-19T16:47:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "ID"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NH"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CT"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "SC"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-02",
      "state": "MS"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-02",
      "state": "CO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AZ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "WA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "VT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2918is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2918\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Whitehouse (for himself, Mr. Risch , Mrs. Shaheen , Mr. Grassley , Mr. Blumenthal , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act to improve the implementation of the seizure of Russian sovereign assets for the benefit of Ukraine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the REPO for Ukrainians Implementation Act of 2025 or the REPO Implementation Act of 2025 .\n#### 2. Recognition of Porto Declaration of Organization for Security and Co-operation in Europe\nSection 101(a) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(10) Every member of the European Union, including Belgium, and all but one member of the G7, are also participating states of the Organization for Security and Cooperation in Europe. (11) On July 3, 2025, the Parliamentary Assembly of the Organization for Security and Cooperation in Europe adopted unanimously in plenary session the Porto Declaration, which [c]alls on OSCE participating States to unlock the full value of an estimated U.S. $300 billion in Russian sovereign assets frozen across the region by repurposing the underlying principal, in sizeable increments and on a regular and timely schedule, for Ukraine until the Russian Federation ends its aggression and agrees to compensate Ukraine for damages directly resulting from the war . .\n#### 3. Transfer of assets to Ukraine Support Fund\nSection 104(b)(2) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin the heading, by striking Vesting and inserting Status of assets ;\n**(2)**\nby striking For funds confiscated and inserting the following:\n(A) Vesting of confiscated funds For funds confiscated ; and\n**(3)**\nby adding at the end the following:\n(B) Transfer of funds not confiscated For the purpose of placing Russian aggressor state sovereign assets into an interest-bearing account, the President may transfer such funds into the Ukraine Support Fund without confiscating such funds. .\n#### 4. Investment of amounts in Ukraine Support Fund\n##### (a) In general\nSection 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking of any funds and inserting the following: \u201cof\u2014\n(A) any funds ;\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(B) any amounts that may be credited to the account under paragraph (3). ; and\n**(2)**\nby adding at the end the following:\n(3) Investment of amounts (A) Investment of amounts The Secretary of the Treasury shall invest such portion of the account established under paragraph (1) as is not required to meet current withdrawals in interest-bearing obligations of the United States or in obligations guaranteed as to both principal and interest by the United States. (B) Interest and proceeds The interest on, and the proceeds from the sale or redemption of, any obligations held in the account established under paragraph (1) shall be credited to and form a part of the account. .\n##### (b) Implementation\nThe President shall ensure that funds in the Ukraine Support Fund established under section 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act are invested as required by paragraph (3) of that section, as added by subsection (a), by not later than the date that is 45 days after the date of the enactment of this Act.\n#### 5. Quarterly obligation of funds in Ukraine Support Fund to benefit Ukraine\n##### (a) In general\nSection 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(4) Quarterly obligations (A) In general Not less frequently than every 90 days while funds remain in the Ukraine Support Fund, the Secretary of State may obligate and expend, from the Fund, an amount that is not less than $250,000,000 (except as provided by subparagraph (B)) for the purpose of providing assistance to Ukraine under this subsection. (B) Final amounts in Fund When less than $250,000,000 remains in the Fund, the Secretary of State may obligate and expend the remaining amount for the purpose of providing assistance to Ukraine under this subsection. .\n##### (b) Implementation\nIt is the sense of Congress that the President should ensure that the first obligation of amounts pursuant to paragraph (4) of section 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act, as added by subsection (a), occurs not later than the date that is 60 days after the date on which Russian sovereign assets are deposited in the Ukraine Support Fund.\n#### 6. Engagement with certain foreign countries\n##### (a) In general\nTitle II of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n109. Engagement with foreign countries (a) Reports required (1) Covered country report Not later than 90 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (2) Report on non-covered countries Not later than 270 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the foreign countries that are not covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (3) Form The reports required by paragraphs (1) and (2) shall be submitted in unclassified form but may include a classified annex. (b) Sense of Congress on engagement Not later than 30 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the Secretary of State, in coordination with the Secretary of the Treasury, should commence a robust, sustained, diplomatic effort to persuade the government of each covered country to begin repurposing, on a quarterly basis, an amount that is not less than 5 percent of the Russian sovereign assets located in that country for the benefit of Ukraine. (c) Covered country defined In this section, the term covered country means Australia and any country that is a member of the G7 or the European Union, other than the United States. .\n##### (b) Clerical amendment\nThe table of contents in section 1 of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by inserting after the item relating to section 108 the following:\nSec. 109. Engagement with foreign countries. .\n#### 7. Modification of judicial review provision\nSection 104(k) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by striking this section each place it appears and inserting this division .\n#### 8. Technical corrections\nThe Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin section 2(2), by striking paragraph (7) and inserting paragraph (6) ;\n**(2)**\nin section 101(a)\u2014\n**(A)**\nin paragraph (4), by striking deplore[d] and inserting [d]eplore[d] ; and\n**(B)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking a resolution and inserting Resolution ES\u201311/5 ;\n**(3)**\nin section 102(6), by striking the period at the end and inserting a semicolon;\n**(4)**\nin section 103(a), in the matter preceding paragraph (1), by striking section 104(j) and inserting section 104(l) ;\n**(5)**\nin section 104\u2014\n**(A)**\nin subsection (a), by striking section 501.603(b)(ii) and inserting section 501.603(b)(1)(ii) ;\n**(B)**\nin subsection (d)(2), by striking accounts and inserting account ; and\n**(C)**\nin subsection (f)(1), by striking Funds and inserting funds ; and\n**(6)**\nin section 105\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by striking section 104(c) and inserting section 104(d) ;\n**(B)**\nin subsection (b), by striking section 104(f) and inserting section 104(g) ; and\n**(C)**\nin subsection (f), by striking subsection (c)(2) and inserting subsection (c) .",
      "versionDate": "2025-09-19",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2918rs.xml",
      "text": "II\nCalendar No. 243\n119th CONGRESS\n1st Session\nS. 2918\nIN THE SENATE OF THE UNITED STATES\nSeptember 19 (legislative day, September 16), 2025 Mr. Whitehouse (for himself, Mr. Risch , Mrs. Shaheen , Mr. Grassley , Mr. Blumenthal , Mr. Graham , Mr. Wicker , Mr. Bennet , Mr. Cornyn , Mr. Gallego , Ms. Cantwell , and Mr. Crapo ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , without amendment\nA BILL\nTo amend the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act to improve the implementation of the seizure of Russian sovereign assets for the benefit of Ukraine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the REPO for Ukrainians Implementation Act of 2025 or the REPO Implementation Act of 2025 .\n#### 2. Recognition of Porto Declaration of Organization for Security and Co-operation in Europe\nSection 101(a) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(10) Every member of the European Union, including Belgium, and all but one member of the G7, are also participating states of the Organization for Security and Cooperation in Europe. (11) On July 3, 2025, the Parliamentary Assembly of the Organization for Security and Cooperation in Europe adopted unanimously in plenary session the Porto Declaration, which [c]alls on OSCE participating States to unlock the full value of an estimated U.S. $300 billion in Russian sovereign assets frozen across the region by repurposing the underlying principal, in sizeable increments and on a regular and timely schedule, for Ukraine until the Russian Federation ends its aggression and agrees to compensate Ukraine for damages directly resulting from the war . .\n#### 3. Transfer of assets to Ukraine Support Fund\nSection 104(b)(2) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin the heading, by striking Vesting and inserting Status of assets ;\n**(2)**\nby striking For funds confiscated and inserting the following:\n(A) Vesting of confiscated funds For funds confiscated ; and\n**(3)**\nby adding at the end the following:\n(B) Transfer of funds not confiscated For the purpose of placing Russian aggressor state sovereign assets into an interest-bearing account, the President may transfer such funds into the Ukraine Support Fund without confiscating such funds. .\n#### 4. Investment of amounts in Ukraine Support Fund\n##### (a) In general\nSection 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking of any funds and inserting the following: \u201cof\u2014\n(A) any funds ;\n**(B)**\nby striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(B) any amounts that may be credited to the account under paragraph (3). ; and\n**(2)**\nby adding at the end the following:\n(3) Investment of amounts (A) Investment of amounts The Secretary of the Treasury shall invest such portion of the account established under paragraph (1) as is not required to meet current withdrawals in interest-bearing obligations of the United States or in obligations guaranteed as to both principal and interest by the United States. (B) Interest and proceeds The interest on, and the proceeds from the sale or redemption of, any obligations held in the account established under paragraph (1) shall be credited to and form a part of the account. .\n##### (b) Implementation\nThe President shall ensure that funds in the Ukraine Support Fund established under section 104(d) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act are invested as required by paragraph (3) of that section, as added by subsection (a), by not later than the date that is 45 days after the date of the enactment of this Act.\n#### 5. Quarterly obligation of funds in Ukraine Support Fund to benefit Ukraine\n##### (a) In general\nSection 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n(4) Quarterly obligations (A) In general Not less frequently than every 90 days while funds remain in the Ukraine Support Fund, the Secretary of State may obligate and expend, from the Fund, an amount that is not less than $250,000,000 (except as provided by subparagraph (B)) for the purpose of providing assistance to Ukraine under this subsection. (B) Final amounts in Fund When less than $250,000,000 remains in the Fund, the Secretary of State may obligate and expend the remaining amount for the purpose of providing assistance to Ukraine under this subsection. .\n##### (b) Implementation\nIt is the sense of Congress that the President should ensure that the first obligation of amounts pursuant to paragraph (4) of section 104(f) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act, as added by subsection (a), occurs not later than the date that is 60 days after the date on which Russian sovereign assets are deposited in the Ukraine Support Fund.\n#### 6. Engagement with certain foreign countries\n##### (a) In general\nTitle II of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by adding at the end the following:\n109. Engagement with foreign countries (a) Reports required (1) Covered country report Not later than 90 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (2) Report on non-covered countries Not later than 270 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the President shall submit to the appropriate congressional committees a report specifying\u2014 (A) the foreign countries that are not covered countries in which Russian sovereign assets are located; (B) the amount of such assets in each such country; and (C) a description of such assets, including\u2014 (i) whether or not such assets are frozen, blocked, or immobilized; and (ii) whether or not such assets are accruing interest. (3) Form The reports required by paragraphs (1) and (2) shall be submitted in unclassified form but may include a classified annex. (b) Sense of Congress on engagement Not later than 30 days after the date of the enactment of the REPO for Ukrainians Implementation Act of 2025 , the Secretary of State, in coordination with the Secretary of the Treasury, should commence a robust, sustained, diplomatic effort to persuade the government of each covered country to begin repurposing, on a quarterly basis, an amount that is not less than 5 percent of the Russian sovereign assets located in that country for the benefit of Ukraine. (c) Covered country defined In this section, the term covered country means Australia and any country that is a member of the G7 or the European Union, other than the United States. .\n##### (b) Clerical amendment\nThe table of contents in section 1 of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by inserting after the item relating to section 108 the following:\nSec. 109. Engagement with foreign countries. .\n#### 7. Modification of judicial review provision\nSection 104(k) of the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended by striking this section each place it appears and inserting this division .\n#### 8. Technical corrections\nThe Rebuilding Economic Prosperity and Opportunity for Ukrainians Act (division F of Public Law 118\u201350 ; 22 U.S.C. 9521 note) is amended\u2014\n**(1)**\nin section 2(2), by striking paragraph (7) and inserting paragraph (6) ;\n**(2)**\nin section 101(a)\u2014\n**(A)**\nin paragraph (4), by striking deplore[d] and inserting [d]eplore[d] ; and\n**(B)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking a resolution and inserting Resolution ES\u201311/5 ;\n**(3)**\nin section 102(6), by striking the period at the end and inserting a semicolon;\n**(4)**\nin section 103(a), in the matter preceding paragraph (1), by striking section 104(j) and inserting section 104(l) ;\n**(5)**\nin section 104\u2014\n**(A)**\nin subsection (a), by striking section 501.603(b)(ii) and inserting section 501.603(b)(1)(ii) ;\n**(B)**\nin subsection (d)(2), by striking accounts and inserting account ; and\n**(C)**\nin subsection (f)(1), by striking Funds and inserting funds ; and\n**(6)**\nin section 105\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by striking section 104(c) and inserting section 104(d) ;\n**(B)**\nin subsection (b), by striking section 104(f) and inserting section 104(g) ; and\n**(C)**\nin subsection (f), by striking subsection (c)(2) and inserting subsection (c) .",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-10-24",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "5835",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REPO Implementation Act of 2025",
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
            "name": "Conflicts and wars",
            "updateDate": "2026-04-01T20:21:53Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2026-04-01T20:22:38Z"
          },
          {
            "name": "Europe",
            "updateDate": "2026-04-01T20:21:39Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2026-04-01T20:22:26Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2026-04-01T20:22:16Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-04-01T20:21:45Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2026-04-01T20:21:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:06:34Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2918is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2918rs.xml"
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
      "title": "REPO Implementation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T11:03:21Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "REPO Implementation Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "REPO for Ukrainians Implementation Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REPO Implementation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REPO for Ukrainians Implementation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-09T04:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Rebuilding Economic Prosperity and Opportunity for Ukrainians Act to improve the implementation of the seizure of Russian sovereign assets for the benefit of Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-09T04:48:16Z"
    }
  ]
}
```
