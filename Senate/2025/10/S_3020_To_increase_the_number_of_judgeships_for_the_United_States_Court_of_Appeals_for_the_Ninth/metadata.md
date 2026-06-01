# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3020?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3020
- Title: Judicial Efficiency Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 3020
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2025-12-08T14:31:53Z
- Update date including text: 2025-12-08T14:31:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3020",
    "number": "3020",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Judicial Efficiency Improvement Act",
    "type": "S",
    "updateDate": "2025-12-08T14:31:53Z",
    "updateDateIncludingText": "2025-12-08T14:31:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T19:16:27Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "MT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "ID"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3020is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3020\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Sullivan (for himself, Mr. Crapo , Mr. Daines , Ms. Murkowski , Mr. Risch , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo increase the number of judgeships for the United States Court of Appeals for the Ninth Circuit and certain district courts of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Judicial Efficiency Improvement Act .\n#### 2. Definitions\nIn this Act:\n**(1) Former ninth circuit**\nThe term former ninth circuit means the ninth judicial circuit of the United States as in existence on the day before the effective date of this Act.\n**(2) New ninth circuit**\nThe term new ninth circuit means the ninth judicial circuit of the United States established by the amendment made by section 3(2)(A).\n**(3) Twelfth circuit**\nThe term twelfth circuit means the twelfth judicial circuit of the United States established by the amendment made by section 3(2)(B).\n#### 3. Number and composition of circuits\nSection 41 of title 28, United States Code, is amended\u2014\n**(1)**\nin the matter preceding the table, by striking thirteen and inserting fourteen ; and\n**(2)**\nin the table\u2014\n**(A)**\nby striking the item relating to the ninth circuit and inserting the following:\nNinth California, Guam, Hawaii, Northern Mariana Islands. ;\nand\n**(B)**\nby inserting after the item relating to the eleventh circuit the following:\nTwelfth Alaska, Arizona, Idaho, Montana, Nevada, Oregon, Washington. .\n#### 4. Circuit court judgeships\n##### (a) New Judgeships\nThe President shall appoint, by and with the advice and consent of the Senate, 2 additional circuit judges for the new ninth circuit, whose official duty station shall be in California.\n##### (b) Effective Date\nThis section shall take effect on the date of enactment of this Act.\n#### 5. Number of circuit judges\nThe table in section 44(a) of title 28, United States Code, is amended\u2014\n**(1)**\nby striking the item relating to the ninth circuit and inserting the following:\nNinth 18 ;\nand\n**(2)**\nby inserting after the item relating to the eleventh circuit the following:\nTwelfth 13 .\n#### 6. Places of circuit court\nThe table in section 48(a) of title 28, United States Code, is amended\u2014\n**(1)**\nby striking the item relating to the ninth circuit and inserting the following:\nNinth Honolulu, Pasadena, San Francisco. ;\nand\n**(2)**\nby inserting after the item relating to the eleventh circuit the following:\nTwelfth Las Vegas, Phoenix, Portland, Seattle. .\n#### 7. Location of Twelfth Circuit headquarters\nThe offices of the Circuit Executive of the Twelfth Circuit and the Clerk of the Court of the Twelfth Circuit shall be located in Seattle, Washington.\n#### 8. Assignment of circuit judges\nEach circuit judge of the former ninth circuit who is in regular active service and whose official duty station on the day before the effective date of this Act\u2014\n**(1)**\nis in California, Guam, Hawaii, or the Northern Mariana Islands shall be a circuit judge of the new ninth circuit as of that effective date; and\n**(2)**\nis in Alaska, Arizona, Idaho, Montana, Nevada, Oregon, or Washington shall be a circuit judge of the twelfth circuit as of that effective date.\n#### 9. Election of assignment by senior judges\nEach judge who is a senior circuit judge of the former ninth circuit on the day before the effective date of this Act\u2014\n**(1)**\nmay elect to be assigned to the new ninth circuit or the twelfth circuit as of that effective date; and\n**(2)**\nshall notify the Director of the Administrative Office of the United States Courts of the election made under paragraph (1).\n#### 10. Seniority of judges\nThe seniority of each judge who is assigned under section 8 or elects to be assigned under section 9 shall run from the date of commission of the judge as a judge of the former ninth circuit.\n#### 11. Application to cases\nThe following apply to any case in which, on the day before the effective date of this Act, an appeal or other proceeding has been filed with the former ninth circuit:\n**(1)**\nExcept as provided in paragraph (3), if the matter has been submitted for decision, further proceedings with respect to the matter shall be had in the same manner and with the same effect as if this Act had not been enacted.\n**(2)**\nIf the matter has not been submitted for decision, the appeal or proceeding, together with the original papers, printed records, and record entries duly certified, shall, by appropriate orders, be transferred to the court to which the matter would have been submitted had this Act been in full force and effect on the date on which the appeal was taken or other proceeding commenced, and further proceedings with respect to the case shall be had in the same manner and with the same effect as if the appeal or other proceeding had been filed in that court.\n**(3)**\nIf a petition for rehearing en banc is pending on or after the effective date of this Act, the petition shall be considered by the court of appeals to which the petition would have been submitted had this Act been in full force and effect on the date on which the appeal or other proceeding was filed with the court of appeals.\n#### 12. Temporary assignment of circuit judges among circuits\nSection 291 of title 28, United States Code, is amended by adding at the end the following:\n(c) The chief judge of the United States Court of Appeals for the Ninth Circuit may, in the public interest and upon request by the chief judge of the United States Court of Appeals for the Twelfth Circuit, designate and assign temporarily any circuit judge of the Ninth Circuit to act as circuit judge in the Twelfth Circuit. (d) The chief judge of the United States Court of Appeals for the Twelfth Circuit may, in the public interest and upon request by the chief judge of the United States Court of Appeals for the Ninth Circuit, designate and assign temporarily any circuit judge of the Twelfth Circuit to act as circuit judge in the Ninth Circuit. .\n#### 13. Temporary assignment of district judges among circuits\nSection 292 of title 28, United States Code, is amended by adding at the end the following:\n(f) The chief judge of the United States Court of Appeals for the Ninth Circuit may in the public interest\u2014 (1) upon request by the chief judge of the United States Court of Appeals for the Twelfth Circuit, designate and assign one or more district judges of the Ninth Circuit to sit upon the Court of Appeals of the Twelfth Circuit, or a division thereof, whenever the business of that court so requires; and (2) designate and assign temporarily any district judge of the Ninth Circuit to hold a district court in any district within the Twelfth Circuit. (g) The chief judge of the United States Court of Appeals for the Twelfth Circuit may in the public interest\u2014 (1) upon request by the chief judge of the United States Court of Appeals for the Ninth Circuit, designate and assign one or more district judges of the Twelfth Circuit to sit upon the Court of Appeals of the Ninth Circuit, or a division thereof, whenever the business of that court so requires; and (2) designate and assign temporarily any district judge of the Twelfth Circuit to hold a district court in any district within the Ninth Circuit. (h) Any designation or assignment under subsection (f) or (g) shall be in conformity with the rules or orders of the court of appeals of, or the district within, as applicable, the circuit to which the judge is designated or assigned. .\n#### 14. Additional district judges for the district courts\n##### (a) Additional judgeships\n**(1) 2025**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the central district of California;\n**(ii)**\n1 additional district judge for the eastern district of California;\n**(iii)**\n1 additional district judge for the northern district of California;\n**(iv)**\n1 additional district judge for the district of Delaware;\n**(v)**\n1 additional district judge for the middle district of Florida;\n**(vi)**\n1 additional district judge for the southern district of Indiana;\n**(vii)**\n1 additional district judge for the northern district of Iowa;\n**(viii)**\n1 additional district judge for the district of New Jersey;\n**(ix)**\n1 additional district judge for the southern district of New York;\n**(x)**\n1 additional district judge for the eastern district of Texas; and\n**(xi)**\n1 additional district judge for the southern district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 15 Eastern 7 Central 28 Southern 13 ;\n**(ii)**\nby striking the item relating to Delaware and inserting the following:\nDelaware 5 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 16 Southern 17 ;\n**(iv)**\nby striking the items relating to Indiana and inserting the following:\nIndiana: Northern 5 Southern 6 ;\n**(v)**\nby striking the items relating to Iowa and inserting the following:\nIowa: Northern 3 Southern 3 ;\n**(vi)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 18 ;\n**(vii)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 15 Western 4 ;\nand\n**(viii)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 12 Southern 20 Eastern 8 Western 13 .\n**(C) Effective date**\nThis paragraph shall take effect on the date of enactment of this Act.\n**(2) 2027**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the district of Arizona;\n**(ii)**\n2 additional district judges for the central district of California;\n**(iii)**\n1 additional district judge for the eastern district of California;\n**(iv)**\n1 additional district judge for the northern district of California;\n**(v)**\n1 additional district judge for the middle district of Florida;\n**(vi)**\n1 additional district judge for the southern district of Florida;\n**(vii)**\n1 additional district judge for the northern district of Georgia;\n**(viii)**\n1 additional district judge for the district of Idaho;\n**(ix)**\n1 additional district judge for the northern district of Texas; and\n**(x)**\n1 additional district judge for the southern district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (1) of this subsection, is amended\u2014\n**(i)**\nby striking the item relating to Arizona and inserting the following:\nArizona 13 ;\n**(ii)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 16 Eastern 8 Central 30 Southern 13 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 17 Southern 18 ;\n**(iv)**\nby striking the items relating to Georgia and inserting the following:\nGeorgia: Northern 12 Middle 4 Southern 3 ;\n**(v)**\nby striking the item relating to Idaho and inserting the following:\nIdaho 3 ;\nand\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 21 Eastern 8 Western 13 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2027.\n**(3) 2029**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the central district of California;\n**(ii)**\n1 additional district judge for the eastern district of California;\n**(iii)**\n1 additional district judge for the northern district of California;\n**(iv)**\n1 additional district judge for the district of Colorado;\n**(v)**\n1 additional district judge for the district of Delaware;\n**(vi)**\n1 additional district judge for the district of Nebraska;\n**(vii)**\n1 additional district judge for the eastern district of New York;\n**(viii)**\n1 additional district judge for the eastern district of Texas;\n**(ix)**\n1 additional district judge for the southern district of Texas; and\n**(x)**\n1 additional district judge for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (2) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 17 Eastern 9 Central 31 Southern 13 ;\n**(ii)**\nby striking the item relating to Colorado and inserting the following:\nColorado 8 ;\n**(iii)**\nby striking the item relating to Delaware and inserting the following:\nDelaware 6 ;\n**(iv)**\nby striking the item relating to Nebraska and inserting the following:\nNebraska 4 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 16 Western 4 ;\nand\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 22 Eastern 9 Western 14 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2029.\n**(4) 2031**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the district of Arizona;\n**(ii)**\n1 additional district judge for the central district of California;\n**(iii)**\n1 additional district judge for the eastern district of California;\n**(iv)**\n1 additional district judge for the northern district of California;\n**(v)**\n1 additional district judge for the southern district of California;\n**(vi)**\n1 additional district judge for the middle district of Florida;\n**(vii)**\n1 additional district judge for the southern district of Florida;\n**(viii)**\n1 additional district judge for the district of New Jersey;\n**(ix)**\n1 additional district judge for the western district of New York; and\n**(x)**\n2 additional district judges for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (3) of this subsection, is amended\u2014\n**(i)**\nby striking the item relating to Arizona and inserting the following:\nArizona 14 ;\n**(ii)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 18 Eastern 10 Central 32 Southern 14 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 18 Southern 19 ;\n**(iv)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 19 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 16 Western 5 ;\nand\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 22 Eastern 9 Western 16 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2031.\n**(5) 2033**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n2 additional district judges for the central district of California;\n**(ii)**\n1 additional district judge for the northern district of California;\n**(iii)**\n1 additional district judge for the district of Colorado;\n**(iv)**\n1 additional district judge for the middle district of Florida;\n**(v)**\n1 additional district judge for the northern district of Florida;\n**(vi)**\n1 additional district judge for the northern district of Georgia;\n**(vii)**\n1 additional district judge for the southern district of New York;\n**(viii)**\n1 additional district judge for the southern district of Texas; and\n**(ix)**\n1 additional district judge for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (4) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 19 Eastern 10 Central 34 Southern 14 ;\n**(ii)**\nby striking the item relating to Colorado and inserting the following:\nColorado 9 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 5 Middle 19 Southern 19 ;\n**(iv)**\nby striking the items relating to Georgia and inserting the following:\nGeorgia: Northern 13 Middle 4 Southern 3 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 30 Eastern 16 Western 5 ;\nand\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 23 Eastern 9 Western 17 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2033.\n**(6) 2035**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n2 additional district judges for the central district of California;\n**(ii)**\n1 additional district judge for the northern district of California;\n**(iii)**\n1 additional district judge for the southern district of California;\n**(iv)**\n1 additional district judge for the middle district of Florida;\n**(v)**\n1 additional district judge for the southern district of Florida;\n**(vi)**\n1 additional district judge for the district of New Jersey;\n**(vii)**\n1 additional district judge for the eastern district of New York; and\n**(viii)**\n2 additional district judges for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (5) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 20 Eastern 10 Central 36 Southern 15 ;\n**(ii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 5 Middle 20 Southern 20 ;\n**(iii)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 20 ;\n**(iv)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 30 Eastern 17 Western 5 ;\nand\n**(v)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 23 Eastern 9 Western 19 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2035.\n##### (b) Temporary judgeships\n**(1) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(A)**\n2 additional district judges for the eastern district of Oklahoma; and\n**(B)**\n1 additional district judge for the northern district of Oklahoma.\n**(2) Vacancies not filled**\nThe first vacancy in the office of district judge in each of the offices of district judge authorized by this subsection, occurring 5 years or more after the confirmation date of the judge named to fill the temporary district judgeship created in the applicable district by this subsection, shall not be filled.\n**(3) Effective date**\nThis subsection shall take effect on the date of enactment of this Act.\n##### (c) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section and the amendments made by this section\u2014\n**(A)**\nfor each of fiscal years 2025 and 2026, $12,965,330;\n**(B)**\nfor each of fiscal years 2027 and 2028, $23,152,375;\n**(C)**\nfor each of fiscal years 2029 and 2030, $32,413,325;\n**(D)**\nfor each of fiscal years 2031 and 2032, $42,600,370;\n**(E)**\nfor each of fiscal years 2033 and 2034, $51,861,320; and\n**(F)**\nfor fiscal year 2035 and each fiscal year thereafter, $61,122,270.\n**(2) Inflation adjustment**\nFor each fiscal year described in paragraph (1), the amount authorized to be appropriated for such fiscal year shall be increased by the percentage by which\u2014\n**(A)**\nthe Consumer Price Index for the previous fiscal year, exceeds\n**(B)**\nthe Consumer Price Index for the fiscal year preceding the fiscal year described in subparagraph (A).\n**(3) Definition**\nIn this subsection, the term Consumer Price Index means the Consumer Price Index for All Urban Consumers (all items, United States city average), published by the Bureau of Labor Statistics of the Department of Labor.\n#### 15. Administration\n##### (a) Transition authority\nThe court of appeals for the ninth circuit as constituted on the day before the effective date of this Act may take any administrative action that is required to carry out this Act and the amendments made by this Act.\n##### (b) Administrative termination\nThe court described in subsection (a) shall cease to exist for administrative purposes 2 years after the date of enactment of this Act.\n#### 16. Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this Act, including funds for additional court facilities.\n#### 17. Effective date\nExcept as provided in section 4(b) and 14, this Act and the amendments made by this Act shall take effect 1 year after the date of enactment of this Act.",
      "versionDate": "2025-10-21",
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
        "name": "Law",
        "updateDate": "2025-12-08T14:31:53Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3020is.xml"
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
      "title": "Judicial Efficiency Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Judicial Efficiency Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the number of judgeships for the United States Court of Appeals for the Ninth Circuit and certain district courts of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-25T07:33:19Z"
    }
  ]
}
```
