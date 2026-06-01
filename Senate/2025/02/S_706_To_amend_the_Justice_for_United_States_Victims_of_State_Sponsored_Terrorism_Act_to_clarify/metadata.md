# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/706
- Title: American Victims of Terrorism Compensation Act
- Congress: 119
- Bill type: S
- Bill number: 706
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-12-05T22:49:32Z
- Update date including text: 2025-12-05T22:49:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/706",
    "number": "706",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "American Victims of Terrorism Compensation Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:32Z",
    "updateDateIncludingText": "2025-12-05T22:49:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T16:34:38Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "ND"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s706is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 706\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Cornyn (for himself, Mr. Blumenthal , Mr. Cramer , Mr. Schumer , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Justice for United States Victims of State Sponsored Terrorism Act to clarify and supplement the funding sources for United States victims of state-sponsored terrorism to ensure consistent and meaningful distributions from the United States Victims of State Sponsored Terrorism Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Victims of Terrorism Compensation Act .\n#### 2. Transfer of certain funds into united states victims of state sponsored terrorism fund\n##### (a) In general\nSection 404 of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144 ) is amended\u2014\n**(1)**\nin subsection (d)(4), by adding at the end the following:\n(E) Fifth-round payments All fifth-round payments required to be authorized by the Special Master on or before January 1, 2025, shall be distributed to eligible claimants not later than March 14, 2025, or, if an eligible claimant has not provided the Special Master with the payment information required for distribution, as soon as practicable after the date of receipt by the Special Master of such information. ; and\n**(2)**\nin subsection (e)(2), by adding at the end the following:\n(C) Certain assigned and forfeited assets (i) Binance holdings limited (I) In general (aa) Already deposited The sum of $898,619,225, corresponding to the funds, and the net proceeds from the sale of property, forfeited to the United States from or in connection with the plea agreement in the proceedings captioned as United States v. Binance Holdings Limited, No. 2:23\u2013cr\u201300178 (RAJ) (W.D. Wash. filed Nov. 14, 2023), already deposited into the Fund. (bb) Additional funds The sum of $1,912,031,763, corresponding to a portion of the funds, and the net proceeds from the sale of property, forfeited or paid to the United States arising from or in connection with the proceedings described in item (aa) or any related civil or administrative proceedings. (cc) Interest All interest earned on the amounts described in item (aa) or (bb) from the date of such forfeiture or payment. (II) Deposit in cvf The sum of $1,505,475,575, from the funds, and the net proceeds from the sale of property, paid to the United States arising from or in connection with proceedings described in subclause (I)(aa) shall be deposited into the Crime Victims Fund established under section 1402 of the Victims of Crime Act of 1984 ( 34 U.S.C. 20101 ). (III) Timing An agency of the United States shall deposit or transfer into the Fund any amount paid by a defendant in such proceedings that is required to be deposited into the Fund pursuant to subclause (I), plus any interest thereon, not later than the later of\u2014 (aa) 30 days after the receipt of such amount by the agency; or (bb) 15 days after the date of enactment of this subparagraph. (ii) Doj assets forfeiture fund (I) In general Fifty percent of the excess unobligated balance, as defined in section 524(c)(8) of title 28, United States Code, of the Department of Justice Assets Forfeiture Fund established under 524(c)(1) of that title, determined on the later of January 31, or the date of enactment of a final appropriations Act for each fiscal year, to be transferred annually thereafter not later than 30 days after the date of such determination, plus 50 percent of any interest amount earned on the investment of any balance of the Assets Forfeiture Fund as of that date. (II) Transfers No transfer pursuant to this subparagraph shall count against any limitation on the use of the excess unobligated balances described in subclause (I) as provided in an annual appropriations Act or other legislation. (III) Exclusion of rescissions for fiscal year after determination of amount For purposes of subclause (I), the amount of the unobligated balance of the Department of Justice Asset Forfeiture Fund, as of September 30 of a fiscal year, shall be determined without regard to any rescission of amounts in the fund for the next fiscal year included in an appropriation Act referred to in section 105 of title 1, United States Code, including any anticipated or potential rescission and any rescission given continuing effect for such next fiscal year under an Act making continuing appropriations for such next fiscal year. (iii) Treasury forfeiture fund (I) In general Fifty percent of the excess unobligated balance of the Department of the Treasury Forfeiture Fund established under section 9705 of title 31, United States Code, determined on the later of January 31, or the date of enactment of a final appropriations Act for each fiscal year, to be transferred annually thereafter not later than 30 days after such determination, plus 50 percent of any interest amount earned on the investment of any balance of the Treasury Forfeiture Fund as of that date. (II) Transfers No transfer pursuant to this subparagraph shall count against any limitation on the use of excess unobligated balances described in subclause (I) as provided in an annual appropriations Act or other legislation. (III) Definition of excess unobligated balance (aa) In general In this clause, the term excess unobligated balance means the difference between\u2014 (AA) the unobligated balance of the Department of the Treasury Forfeiture Fund, as of September 30 of the fiscal year before the date specified in subclause (I); and (BB) the amount that is required to be retained in the Department of the Treasury Forfeiture Fund to ensure the availability of amounts in the fiscal year after the fiscal year described in subitem (AA) for the purposes for which amounts in the fund are authorized to be used. (bb) Exclusion of rescissions for fiscal year after determination of amount For purposes of subclause (I), the amount of the unobligated balance of the Department of the Treasury Forfeiture Fund, as of September 30 of a fiscal year, shall be determined without regard to any rescission of amounts in the fund for the next fiscal year included in an appropriation Act referred to in section 105 of title 1, United States Code, including any anticipated or potential rescission and any rescission given continuing effect for such next fiscal year under an Act making continuing appropriations for such next fiscal year. (D) Interest All interest earned on any amount deposited or to be deposited into the Fund pursuant to this section, the American Victims of Terrorism Compensation Act, or an amendment made by that Act, following receipt of such amount by any agency of the United States, including all interest earned on the amounts described in subparagraph (C)(i). .\n##### (b) Rule of construction\nNothing in the amendments made by subsection (a) shall be construed to harm, jeopardize, or impair any amounts previously identified for equitable sharing with law enforcement or to limit the right of a direct crime victim to receive restitution ordered by a court before the date of enactment of this Act with respect to any offense in a matter or proceeding from which amounts are to be deposited into the Fund pursuant to the amendments made by subsection (a).\n#### 3. Timing of deposit of penalties and fines into the united states victims of state sponsored terrorism fund\n##### (a) Forfeited funds and property\nSection 404(e)(2)(A) of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144(e)(2)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking forfeited or ;\n**(2)**\nin clause (ii), by striking forfeited or ; and\n**(3)**\nby adding at the end the following:\n(iii) Forfeitures (I) In general All funds, and the net proceeds from the sale of property, forfeited to the United States after the date of enactment of the American Victims of Terrorism Compensation Act, in a matter or proceeding arising from a violation of any license, order, regulation or prohibition issued under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) or the Trading with the Enemy Act (50 U.S.C. App. 1 et seq.) and all funds, and the net proceeds from the sale of property, forfeited to the United States after the date of enactment of the American Victims of Terrorism Compensation Act, in a matter or proceeding involving, or relating to, or arising from the actions of, or doing business with, or acting on behalf of, a state sponsor of terrorism, without regard to the nature of the offense. (II) Scope All funds and net proceeds described in this clause shall be deposited or transferred into the Fund if the state sponsor of terrorism was so designated at the time of the penalty or fine, at any time during the course of any related legal proceedings, or at the time of any related conduct. (III) Rules of construction Nothing in this clause shall be construed to limit any rights to court-ordered restitution of any direct crime victim of an offense in a matter or proceeding from which amounts are to be deposited into the Fund pursuant to this subparagraph. Nothing in the American Victims of Terrorism Compensation Act or an amendment made by that Act that clarifies the scope of forfeiture proceeds to be deposited into the Fund shall be construed to impact the scope or interpretation of criminal or civil penalties or fines that are required to be deposited into the Fund under clauses (i) and (ii) of this subparagraph, which scope is the subject of pending litigation and shall be addressed in such litigation or by future legislation as warranted, including as informed by the report by the Comptroller General of the United States regarding proceeds available for deposit to the Fund required under subsection (b)(1)(A)(v). (iv) Timing An agency of the United States shall deposit or transfer into the Fund all funds, and the net proceeds from the sale of property, forfeited or paid to the United States described in this subparagraph not later than the later of\u2014 (I) 60 days after the receipt of such amount by the agency; or (II) 30 days after the date of enactment of this clause. .\n#### 4. Annual payments\nSection 404(d)(4) of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144(d)(4) ) is amended by striking subparagraph (A) and inserting the following:\n(A) In general Except as provided in subparagraphs (B), (C), and (D), on January 1, 2026, and January 1 of each calendar year thereafter, the Special Master or the Attorney General shall authorize additional payments on a pro rata basis to those claimants with eligible claims under subsection (c)(2) to include all amounts received as of that date by any agency of the United States that qualifies for deposit or transfer into the Fund, plus all interest earned from the date of receipt of any such amounts through the date of deposit or transfer into the Fund that has not already been distributed pursuant to this subsection and is not required for the payment of administrative costs or compensation as set forth in subparagraphs (B) and (C) of subsection (b)(1). All authorized payments shall be distributed to the eligible claimants as soon as practicable in the calendar year of authorization, or, if the Special Master or Attorney General authorizes payments prior to January 1, not later than 1 year after the date of such authorization. .\n#### 5. Report of fund activity\nSection 404(b)(1)(A) of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144(b)(1)(A) ) is amended by adding at the end the following:\n(iv) Attorney general report (I) Report On January 31 of each year, the Special Master shall submit to the chairman and ranking minority member of the Committee on the Judiciary of the Senate and the chairman and ranking minority member of the Committee on the Judiciary of the House of Representatives a report on the balance and activity of the Fund, which shall include\u2014 (aa) the total amount in the Fund at the end of the preceding fiscal year; (bb) deposits into the Fund during the preceding fiscal year sufficient to identify the source, including, if applicable, the case name and the amount of each deposit, except to the extent that any sealing order requires any portion of such information to remain confidential; (cc) disbursements from the Fund during the preceding fiscal year sufficient to identify specific amounts disbursed for victim compensation and other purposes, including for administrative costs and use of Department of Justice personnel; (dd) the amount, and the basis for the calculation, of any funds deposited into the Fund from the Department of Justice Assets Forfeiture Fund established under 524(c)(1) of title 28, United States Code, and the Department of the Treasury Forfeiture Fund established under section 9705 of title 31, United States Code, in the prior fiscal year; (ee) an explanation of any amounts not deposited into the Fund as a result of any rule of construction pursuant to this Act or the American Victims of Terrorism Compensation Act; and (ff) an explanation of all amounts from or relating to cases qualifying for deposit under this Act that are not deposited into the Fund as a result of inter-agency credits, administrative costs, or any other reason. (II) Publication Not later than March 1 of each year, the Attorney General shall publish the report required under subclause (I) on the internet website of the Fund. (v) Gao report regarding proceeds available for deposit to the fund Not later than April 1, 2025, the Comptroller General of the United States shall submit to Congress a report, which shall include\u2014 (I) a listing of all funds, and the net proceeds from the sale of property, forfeited or paid to the United States since January 1, 2020, in an amount greater than $10,000,000 as a criminal penalty or fine in any matter, sufficient to identify the source, including, if applicable, the case name and the amount of each forfeiture or payment, except to the extent that any sealing order requires any portion of such information to remain confidential; (II) a listing of all funds, and the net proceeds from the sale of property, forfeited or paid to the United States since January 1, 2020, in an amount greater than $10,000,000 as a civil penalty or fine in any matter, sufficient to identify the source, including, if applicable, the case name and the amount of each forfeiture or payment, except to the extent that any sealing order requires any portion of such information to remain confidential; (III) an explanation of where each amount described in subclause (I) or (II) was deposited, including deposits into the Fund or the Crime Victims Fund, which shall include the nature of each such deposit, and the statutory basis for each such deposit; and (IV) any interest amount earned on each amount described in subclause (I) or (II). (vi) Gao triennial report Not later than January 1, 2027, and every 3 years thereafter, the Comptroller General of the United States shall submit to Congress a report\u2014 (I) evaluating the administration of the Fund and the sufficiency of funding for the Fund; (II) analyzing funding and payment trends; and (III) describing amounts outstanding and unpaid on eligible claims overall, including such amounts disaggregated by victim group and by when victims entered the Fund. .\n#### 6. Administrative costs and use of department of justice personnel\nSection 404(b)(1) of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144(b)(1) ) is amended by striking subparagraph (B) and inserting the following:\n(B) Administrative costs and use of department of justice personnel The Special Master may utilize, as necessary, no more than 10 full-time equivalent Department of Justice personnel to assist in carrying out the duties of the Special Master under this section. Any costs associated with the use of such personnel, and any other administrative costs of carrying out this section, shall be paid from the Fund. .\n#### 7. Additional reports\nSection 404(d)(4)(D)(iv)(IV) of the Justice for United States Victims of State Sponsored Terrorism Act ( 34 U.S.C. 20144(d)(4)(D)(iv)(IV) ) is amended by striking item (bb) and inserting the following:\n(bb) Remaining amounts Not later than 30 days after the date of enactment of the American Victims of Terrorism Compensation Act, all amounts remaining in the lump sum catch-up payment reserve fund in excess of the amounts described in subclauses (I) and (II) of clause (iii) shall be deposited into the Fund under this section, including all interest earned on amounts in the lump sum catch-up payment reserve fund. All such amounts, including interest, shall be included in a supplemental fifth-round distribution to be authorized by the Special Master not later than April 1, 2025, and distributed pursuant to this section not later than June 30, 2025, to all claimants for whom the Special Master authorized fifth-round distributions. .",
      "versionDate": "2025-02-25",
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
        "actionDate": "2025-02-24",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1530",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Victims of Terrorism Compensation Act",
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
            "updateDate": "2025-07-17T19:20:54Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-17T19:20:54Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-07-17T19:20:54Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-07-17T19:20:54Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-07-17T19:20:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T14:00:57Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s706is.xml"
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
      "title": "American Victims of Terrorism Compensation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Victims of Terrorism Compensation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Justice for United States Victims of State Sponsored Terrorism Act to clarify and supplement the funding sources for United States victims of state-sponsored terrorism to ensure consistent and meaningful distributions from the United States Victims of State Sponsored Terrorism Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:29Z"
    }
  ]
}
```
