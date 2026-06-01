# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2719?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2719
- Title: LIFT Homebuyers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2719
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2025-09-23T14:47:04Z
- Update date including text: 2025-09-23T14:47:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2719",
    "number": "2719",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "LIFT Homebuyers Act of 2025",
    "type": "S",
    "updateDate": "2025-09-23T14:47:04Z",
    "updateDateIncludingText": "2025-09-23T14:47:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T17:45:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2719is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2719\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Warner (for himself, Mr. Van Hollen , Mr. Kaine , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a program to provide low- and moderate-income first-time, first-generation homebuyers with access to affordable and sustainable wealth-building home loans.\n#### 1. Short title\nThis Act may be cited as the Low-Income First-Time Homebuyers Act of 2025 or the LIFT Homebuyers Act of 2025 .\n#### 2. Wealth-building home loan program\n##### (a) Establishment of LIFT HOME funds\n**(1) In general**\nThere is established in each Loan Guarantee Agency a fund to be known as the LIFT HOME Fund, into which amounts made available under this section shall be deposited and which shall be used by each Department for carrying out the purposes of this section.\n**(2) Management of Fund**\nThe LIFT HOME Fund of each Loan Guarantee Agency shall be administered and managed by the respective Secretary, who shall establish reasonable and prudent criteria for the management and operation of any amounts in the Fund.\n##### (b) Use of funds\n**(1) Transfer of amounts to Treasury**\nSuch portions of the amount made available to the Secretary of Housing and Urban Development under this section shall be transferred by the Secretary of Housing and Urban Development to the Department of the Treasury in an amount equal to, as determined by the Secretary of the Treasury, in consultation with the Secretary of Housing and Urban Development\u2014\n**(A)**\nthe amount the Secretary of the Treasury estimates to be necessary for the purchase of securities under the Program during the period for which the funds are intended to be available;\n**(B)**\nthe difference between\u2014\n**(i)**\nthe Secretary of the Treasury\u2019s receipts from the sale or other disposition of securities acquired under the Program; and\n**(ii)**\nthe Secretary of the Treasury\u2019s costs in purchasing such securities; and\n**(C)**\nthe Department of the Treasury\u2019s administrative expenses related to the Program.\n**(2) Credit subsidy**\nSuch portion of the amount made available to each Secretary under this section as may be necessary may be used for the cost to the respective Loan Guarantee Agency of guaranteed loans under this section. Such costs, including the costs of modifying such loans, shall be as defined in section 502 of the Congressional Budget Act of 1974 ( 2 U.S.C. 661a ).\n##### (c) Establishment of the LIFT HOME program\nEach Secretary shall establish, and carry out, with respect to any mortgage with a case number issued on or before December 31, 2027, that is subsequently insured or guaranteed by such Secretary, a program to make covered mortgage loans available to eligible homebuyers to purchase a single-family residence for use as their principal residence (referred to in this section as the Program ), under which\u2014\n**(1)**\nthe Secretary of the Treasury\u2014\n**(A)**\nshall act as a purchaser, on behalf of the Secretary of Housing and Urban Development, of securities that are secured by covered mortgage loans;\n**(B)**\nmay designate financial institutions, including banks, savings associations, trust companies, security brokers or dealers, asset managers, investment advisers, and other institutions and such institutions shall\u2014\n**(i)**\nperform all reasonable duties related to this section as a financial agent of the United States as may be required; and\n**(ii)**\nbe paid for such duties using appropriations available to the Secretary of the Treasury to reimburse financial institutions in their capacity as financial agents of the United States;\n**(C)**\nmay use the services of any agency or instrumentality of the United States or component thereof on a reimbursable basis, and any such agency or instrumentality or component thereof is authorized to provide services as requested by the Secretary using all authorities vested in or delegated to that agency, instrumentality, or component;\n**(D)**\nmay manage, and exercise any rights received in connection with, any financial instruments or assets purchased or acquired pursuant to the authorities granted under this section;\n**(E)**\nmay establish and use vehicles to purchase, hold, and sell financial instruments and other assets; and\n**(F)**\nmay issue such regulations and other guidance as may be necessary or appropriate to carry out the authorities or purposes of this section;\n**(2)**\neach Secretary of a Loan Guarantee Agency shall\u2014\n**(A)**\nestablish pricing terms for covered mortgage loans such that the covered mortgage loans carry a monthly mortgage payment of principal and interest that is not more than 110 percent and not less than 100 percent of the monthly payment of principal, interest, and periodic mortgage insurance premium or loan guarantee fee associated with a newly originated 30-year mortgage loan with the same loan balance insured or guaranteed by the Loan Guarantee Agency as determined by each Secretary, or such pricing terms as are determined by each Secretary to be necessary to develop liquidity for securities backed by covered mortgage loans and expand Program participation by eligible homebuyers; and\n**(B)**\nestablish an outreach and counseling program to increase stakeholder awareness of the Program;\n**(3)**\nthe Secretary of Housing and Urban Development shall\u2014\n**(A)**\nin consultation with the Secretary of the Treasury, establish the pricing terms for the purchase of securities guaranteed by the Association secured by covered mortgage loans such that the covered mortgage loans carry a monthly mortgage payment of principal and interest that is not more than 110 percent and not less than 100 percent of the monthly payment of principal, interest, and periodic mortgage insurance premium or loan guarantee fee associated with a newly originated 30-year mortgage loan with the same loan balance insured or guaranteed by the Loan Guarantee Agency, or such pricing terms as are determined by the Secretaries to be necessary to develop liquidity for securities backed by covered mortgage loans and expand Program participation by eligible homebuyers;\n**(B)**\nhave the authority to designate mortgage bankers, financial institutions, including banks, savings associations, trust companies, security brokers or dealers, asset managers, investment advisers, and other institutions and such institutions shall\u2014\n**(i)**\nperform all reasonable duties related to this section as an agent of the United States as may be required; and\n**(ii)**\nbe paid for such duties using appropriations available under this section to the Secretary of Housing and Urban Development to reimburse these entities in their capacity as agents of the United States;\n**(C)**\nhave the authority to use the services of any agency or instrumentality of the United States or component thereof on a reimbursable basis, and any such agency or instrumentality or component thereof is authorized to provide services as requested by the Secretary of Housing and Urban Development using all authorities vested in or delegated to that agency, instrumentality, or component;\n**(D)**\noperate the Program in coordination with the Association, the Federal Housing Administration, the Rural Housing Service, and the Secretary of the Treasury so as to demonstrate feasibility and workability to market participants, including\u2014\n**(i)**\noriginators and servicers of mortgages;\n**(ii)**\nissuers of mortgage-backed securities; and\n**(iii)**\ninvestors; and\n**(E)**\ngain price discovery experience by instructing the Secretary of the Treasury, following consultation with the Secretary of the Treasury to sell acquired securities described in subparagraph (A) as soon as practicable, thereby hastening the development of liquidity for securities backed by covered mortgage loans.\n**(4) GNMA guarantee authority**\nTo carry out the purposes of this section, the Association may enter into new commitments to issue guarantees of securities based on or backed by mortgages insured under this section.\n**(5) GNMA guaranty fee**\nTo carry out the purposes of this section, the Association may collect guaranty fees consistent with section 306(g)(1) of the National Housing Act ( 12 U.S.C. 1721(g)(1) ) that are paid at securitization.\n##### (d) Definitions\nIn this section:\n**(1) Association**\nThe term Association means the Government National Mortgage Association.\n**(2) Covered mortgage loan**\n**(A) HUD**\nThe term covered mortgage loan means, for purposes of the Program established by the Secretary of Housing and Urban Development, a mortgage loan that\u2014\n**(i)**\nis insured or guaranteed by the Federal Housing Administration pursuant to section 203(b) of the National Housing Act ( 12 U.S.C. 1709(b) ), subject to the eligibility criteria set forth in this subsection, and has a case number issued on or before December 31, 2027;\n**(ii)**\nis made for an original term of 20 years or for an original term determined by the Secretary to be necessary to develop liquidity for securities backed by covered mortgage loans and expand Program participation by eligible homebuyers;\n**(iii)**\nsubject to subparagraph (C) of this paragraph and notwithstanding section 203(b)(2)(C) of the National Housing Act ( 12 U.S.C. 1709(b)(2)(C) ), has a mortgage insurance premium of not more than 4 percent of the loan balance that is paid at closing, financed into the principal balance of the loan, paid through an annual premium, or a combination thereof;\n**(iv)**\ninvolves a rate of interest that is fixed over the term of the mortgage loan; and\n**(v)**\nis secured by a single-family residence that is the principal residence of an eligible homebuyer.\n**(B) USDA**\nThe term covered mortgage loan means, for purposes of the Program established by the Secretary of Agriculture, a loan guaranteed under section 502(h) of the Housing Act of 1949 ( 42 U.S.C. 1472(h) ) that\u2014\n**(i)**\nnotwithstanding section 502(h)(7)(A) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(7)(A) ), is made for an original term of 20 years or for an original term determined by the Secretary to be necessary to develop liquidity for securities backed by covered mortgage loans and expand Program participation by eligible homebuyers; and\n**(ii)**\nsubject to subparagraph (C) of this paragraph and notwithstanding section 502(h)(8)(A) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(8)(A) ), has a loan guarantee fee of not more than 4 percent of the principal obligation of the loan.\n**(C) Waiver of mortgage insurance premium requirement**\nEach Secretary, in consultation with the Secretary of the Treasury, and notwithstanding section 502(h)(8)(A) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(8)(A) ) for purposes of the Program established by the Secretary of Agriculture, may waive the mortgage insurance premium cap or loan guarantee fee cap under subparagraphs (A)(iii) and (B)(ii) with respect to covered mortgage loans insured or guaranteed by the Loan Guarantee Agency of which that Secretary is the head if necessary to protect the solvency of the associated insurance fund.\n**(3) Department**\nUnless otherwise specified, the term Department means the Department of Housing and Urban Development or the Department of Agriculture, as appropriate.\n**(4) Eligible homebuyer**\nThe term eligible homebuyer means an individual who\u2014\n**(A)**\nfor purposes of the Program established by the Secretary of Housing and Urban Development\u2014\n**(i)**\nhas an annual household income that is less than or equal to\u2014\n**(I)**\n120 percent of median income for the area, as determined by the Secretary of Housing and Urban Development for\u2014\n**(aa)**\nthe area in which the home to be acquired using such assistance is located; or\n**(bb)**\nthe area in which the place of residence of the homebuyer is located; or\n**(II)**\nif the homebuyer is acquiring an eligible home that is located in a high-cost area, 140 percent of the median income, as determined by the Secretary, for the area within which the eligible home to be acquired using assistance provided under this section is located;\n**(ii)**\nis a first-time homebuyer, as defined in paragraph (6) of this subsection; and\n**(iii)**\nis a first-generation homebuyer as defined in paragraph (5) of this subsection; and\n**(B)**\nfor purposes of the Program established by the Secretary of Agriculture\u2014\n**(i)**\nmeets the applicable requirements in section 502(h) of the Housing Act of 1949 ( 42 U.S.C. 1472(h) ); and\n**(ii)**\nis a first-time homebuyer as defined in paragraph (6) of this subsection and a first-generation homebuyer as defined in paragraph (5) of this subsection.\n**(5) First-generation homebuyer**\nThe term first-generation homebuyer means a homebuyer that, as attested by the homebuyer, is\u2014\n**(A)**\nan individual\u2014\n**(i)**\nwhose living parents or legal guardians do not, to the best of the individual\u2019s knowledge, have any present fee simple ownership interest in a principal residence in any State, excluding ownership of heir property;\n**(ii)**\nif no parents or legal guardians are living upon acquisition of the eligible home to be acquired using such assistance, to the best of the individual\u2019s knowledge, whose parents or legal guardians did not have any ownership interest in a principal residence in any State at the time of their death, excluding ownership of heir property; and\n**(iii)**\nwhose spouse, or domestic partner has not, during the 3-year period ending upon acquisition of the eligible home to be acquired using such assistance, had any present ownership interest in a principal residence in any State, excluding ownership of heir property, whether the individual is a co-borrower on the loan or not; or\n**(B)**\nan individual who has at any time been placed in foster care or institutional care whose spouse or domestic partner has not, during the 3-year period ending upon acquisition of the eligible home to be acquired using such assistance, had any ownership interest in a principal residence in any State, excluding ownership of heir property, whether such individuals are co-borrowers on the loan or not.\n**(6) First-time homebuyer**\nThe term first-time homebuyer means a homebuyer as defined in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ), except that ownership of heir property shall not be treated as owning a home for purposes of determining whether a borrower qualifies as a first-time homebuyer.\n**(7) Heir property**\nThe term heir property means residential property for which title passed by operation of law through intestacy and is held by 2 or more heirs as tenants in common.\n**(8) Loan guarantee agency**\nUnless otherwise specified, the term Loan Guarantee Agency means the Federal Housing Administration of the Department of Housing and Urban Development or the Rural Housing Service of the Department of Agriculture, as appropriate.\n**(9) Secretary**\nUnless otherwise specified, the term Secretary means the Secretary of Housing and Urban Development or the Secretary of Agriculture, as appropriate.\n##### (e) Reliance on borrower attestations\nNo additional documentation beyond the borrower\u2019s attestation shall be required to demonstrate eligibility under paragraph (4) of subsection (d) and no State, eligible entity, or creditor shall be subject to liability, including monetary penalties or requirements to indemnify a Federal agency or repurchase a loan that has been sold or securitized, based on the provision of assistance under this section to a borrower who does not meet the eligibility requirements under paragraph (4) of subsection (d) if the creditor does so in good faith reliance on borrower attestations of eligibility required under such paragraph.\n##### (f) Implementation\nThe Secretary of Housing and Urban Development, the Secretary of Agriculture, and the Secretary of the Treasury shall have authority to issue such regulations or other notices, guidance, forms, instructions, and publications as may be necessary or appropriate to carry out the programs, projects, or activities authorized under this section, including to ensure that such programs, projects, or activities are completed in a timely and effective manner.\n##### (g) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary of Housing and Urban Development and the Secretary of Agriculture such sums as may be necessary to carry out the LIFT HOME Program.",
      "versionDate": "2025-09-04",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-23T14:47:04Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2719is.xml"
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
      "title": "LIFT Homebuyers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIFT Homebuyers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Low-Income First-Time Homebuyers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a program to provide low- and moderate-income first-time, first-generation homebuyers with access to affordable and sustainable wealth-building home loans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:24Z"
    }
  ]
}
```
